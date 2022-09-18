# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.


from fastapi.testclient import TestClient

from main import app

BASE_URL = "nausf-ausf/v1"
UE_AUTHENTICATION_ENDPOINT = f"{BASE_URL}/ue-authentications/"


def test_given_when_then():
    client = TestClient(app)

    response = client.get(f"{UE_AUTHENTICATION_ENDPOINT}")

    response_content = response.json()

    assert response_content == {"a": "b"}
