# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.


import uuid
from unittest.mock import patch

import pytest
from fastapi.testclient import TestClient
from fiveg_core_common_schemas.Uri import Uri
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from api.namf_comm.v1.endpoints.ue_contexts import n1_message_notify
from database.base_class import Base
from database.session import get_db
from main import app
from schemas.N1MessageContainer import N1MessageContainer
from schemas.N1MessageNotification import N1MessageNotification
from schemas.RefToBinaryData import RefToBinaryData

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="function")
def clear_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db


BASE_URL = "namf-comm/v1"
UE_CONTEXTS_ENDPOINT = f"{BASE_URL}/ue-contexts"


def test_given_no_n1_or_n2_message_when_n1n2_message_subscribe_then_400_error_is_raised(clear_db):
    client = TestClient(app)
    ue_context_id = str(uuid.uuid4())

    response = client.post(
        url=f"{UE_CONTEXTS_ENDPOINT}/{ue_context_id}/n1-n2-messages/subscriptions",
        json={},
    )

    response_content = response.json()

    assert response.status_code == 400
    assert (
        response_content["detail"] == "Must specify `n1MessageClass` and/or `n2InformationClass`"
    )


def test_given_bad_n1_message_when_n1n2_message_subscribe_then_400_is_returned(clear_db):
    client = TestClient(app)
    ue_context_id = str(uuid.uuid4())
    ue_n1n2_info_subscription_create_data = {
        "n1MessageClass": "BAD VALUE",
    }

    response = client.post(
        url=f"{UE_CONTEXTS_ENDPOINT}/{ue_context_id}/n1-n2-messages/subscriptions",
        json=ue_n1n2_info_subscription_create_data,
    )

    assert response.status_code == 400


def test_given_n1_message_but_no_n1_uri_when_n1n2_message_subscribe_then_400_error_is_returned(
    clear_db,
):
    client = TestClient(app)
    ue_context_id = str(uuid.uuid4())
    ue_n1n2_info_subscription_create_data = {
        "n1MessageClass": "5GMM",
    }

    response = client.post(
        url=f"{UE_CONTEXTS_ENDPOINT}/{ue_context_id}/n1-n2-messages/subscriptions",
        json=ue_n1n2_info_subscription_create_data,
    )

    response_content = response.json()
    assert response.status_code == 400
    assert (
        response_content["detail"]
        == "Must specify `n1NotifyCallbackUri` when n1MessageClass is selected"
    )


def test_given_n1_message_with_uri_when_n1n2_message_subscribe_then_201_ok_is_returned(clear_db):
    client = TestClient(app)
    ue_context_id = str(uuid.uuid4())
    ue_n1n2_info_subscription_create_data = {
        "n1MessageClass": "5GMM",
        "n1NotifyCallbackUri": "http:banana.com",
    }

    response = client.post(
        url=f"{UE_CONTEXTS_ENDPOINT}/{ue_context_id}/n1-n2-messages/subscriptions",
        json=ue_n1n2_info_subscription_create_data,
    )

    response_content = response.json()
    subscription_id = response_content["n1n2NotifySubscriptionId"]
    assert response.status_code == 201
    assert subscription_id is not None
    assert (
        response.headers["location"]
        == f"/{ue_context_id}/n1-n2-messages/subscriptions/{subscription_id}"
    )


def test_given_n2_message_but_no_n2_uri_when_n1n2_message_subscribe_then_400_error_is_returned(
    clear_db,
):
    client = TestClient(app)
    ue_context_id = str(uuid.uuid4())
    ue_n1n2_info_subscription_create_data = {
        "n2InformationClass": "SM",
    }

    response = client.post(
        url=f"{UE_CONTEXTS_ENDPOINT}/{ue_context_id}/n1-n2-messages/subscriptions",
        json=ue_n1n2_info_subscription_create_data,
    )

    response_content = response.json()
    assert response.status_code == 400
    assert (
        response_content["detail"]
        == "Must specify `n2NotifyCallbackUri` when n2InformationClass is selected"
    )


def test_given_n2_message_with_uri_when_n1n2_message_subscribe_then_201_ok_is_returned(clear_db):
    client = TestClient(app)
    ue_context_id = str(uuid.uuid4())
    ue_n1n2_info_subscription_create_data = {
        "n2InformationClass": "SM",
        "n2NotifyCallbackUri": "http:banana.com",
    }

    response = client.post(
        url=f"{UE_CONTEXTS_ENDPOINT}/{ue_context_id}/n1-n2-messages/subscriptions",
        json=ue_n1n2_info_subscription_create_data,
    )

    response_content = response.json()
    subscription_id = response_content["n1n2NotifySubscriptionId"]
    assert response.status_code == 201
    assert subscription_id is not None
    assert (
        response.headers["location"]
        == f"/{ue_context_id}/n1-n2-messages/subscriptions/{subscription_id}"
    )


def test_given_n1_subscription_not_created_when_n1n2_message_unsubscribe_then_400_error_is_returned(  # noqa: E501
    clear_db,
):
    client = TestClient(app)
    ue_context_id = str(uuid.uuid4())
    subscription_id = str(uuid.uuid4())
    url = f"{UE_CONTEXTS_ENDPOINT}/{ue_context_id}/n1-n2-messages/subscriptions/{subscription_id}"

    response = client.delete(url=url)

    response_content = response.json()
    assert response.status_code == 400
    assert response_content["detail"] == f"Did not find subscription for id {subscription_id}"


def test_given_n1_subscription_when_n1n2_message_unsubscribe_then_204_is_returned(clear_db):
    client = TestClient(app)
    ue_context_id = str(uuid.uuid4())
    ue_n1n2_info_subscription_create_data = {
        "n1MessageClass": "5GMM",
        "n1NotifyCallbackUri": "http:banana.com",
    }
    create_subscription_response = client.post(
        url=f"{UE_CONTEXTS_ENDPOINT}/{ue_context_id}/n1-n2-messages/subscriptions",
        json=ue_n1n2_info_subscription_create_data,
    )
    location = create_subscription_response.headers["location"]

    delete_subscription_response = client.delete(url=f"{UE_CONTEXTS_ENDPOINT}{location}")

    assert delete_subscription_response.status_code == 204


def test_given_n1_subscription_when_n1n2_message_unsubscribe_twice_then_400_is_returned(clear_db):
    client = TestClient(app)
    ue_context_id = str(uuid.uuid4())
    ue_n1n2_info_subscription_create_data = {
        "n1MessageClass": "5GMM",
        "n1NotifyCallbackUri": "http:banana.com",
    }
    create_subscription_response = client.post(
        url=f"{UE_CONTEXTS_ENDPOINT}/{ue_context_id}/n1-n2-messages/subscriptions",
        json=ue_n1n2_info_subscription_create_data,
    )
    location = create_subscription_response.headers["location"]
    subscription_id = location.split("/")[-1]

    client.delete(url=f"{UE_CONTEXTS_ENDPOINT}{location}")
    delete_subscription_response = client.delete(url=f"{UE_CONTEXTS_ENDPOINT}{location}")

    response_content = delete_subscription_response.json()
    assert delete_subscription_response.status_code == 400
    assert response_content["detail"] == f"Did not find subscription for id {subscription_id}"


@patch("requests.post")
def test_given_url_and_n1_message_when_n1_message_notify_then_http_post_is_called(patch_post):
    url = Uri("http://abc.com")

    n1_message_notification = N1MessageNotification(
        n1MessageContainer=N1MessageContainer(
            n1MessageClass="5GMM", n1MessageContent=RefToBinaryData(contentId="whatever")
        )
    )

    n1_message_notify(url=url, n1_message_notification=n1_message_notification)

    patch_post.assert_called_with(url=url, json=n1_message_notification)
