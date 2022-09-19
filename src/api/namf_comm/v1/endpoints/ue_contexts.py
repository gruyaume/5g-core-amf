# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.

import json
import uuid

import requests
from fastapi import APIRouter, Depends, HTTPException, Response
from fiveg_core_common_schemas.Uri import Uri
from sqlalchemy.orm import Session

from crud import crud_subscriptions
from database.session import get_db
from schemas.N1MessageNotification import N1MessageNotification
from schemas.UeContextTransferReqData import UeContextTransferReqData
from schemas.UeContextTransferRspData import UeContextTransferRspData
from schemas.UeN1N2InfoSubscriptionCreateData import UeN1N2InfoSubscriptionCreateData
from schemas.UeN1N2InfoSubscriptionCreatedData import UeN1N2InfoSubscriptionCreatedData

router = APIRouter()


@router.post(
    path="/{ue_context_id}/transfer",
    status_code=200,
    response_model=UeContextTransferRspData,
)
async def ue_context_transfer(
    ue_context_id: str,
    ue_context_transfer_req_data: UeContextTransferReqData,
    response: Response,
    db: Session = Depends(get_db),
):

    return UeContextTransferRspData()


@router.post(
    path="/{ue_context_id}/n1-n2-messages/subscriptions",
    status_code=201,
    response_model=UeN1N2InfoSubscriptionCreatedData,
)
async def n1n2_message_subscribe(
    ue_context_id: str,
    ue_n1n2_info_subscription_create_data: UeN1N2InfoSubscriptionCreateData,
    response: Response,
    db: Session = Depends(get_db),
):
    if (
        not ue_n1n2_info_subscription_create_data.n1MessageClass
        and not ue_n1n2_info_subscription_create_data.n2InformationClass
    ):
        raise HTTPException(
            status_code=400, detail="Must specify `n1MessageClass` and/or `n2InformationClass`"
        )
    if (
        ue_n1n2_info_subscription_create_data.n1MessageClass
        and not ue_n1n2_info_subscription_create_data.n1NotifyCallbackUri
    ):
        raise HTTPException(
            status_code=400,
            detail="Must specify `n1NotifyCallbackUri` when n1MessageClass is selected",
        )
    if (
        ue_n1n2_info_subscription_create_data.n2InformationClass
        and not ue_n1n2_info_subscription_create_data.n2NotifyCallbackUri
    ):
        raise HTTPException(
            status_code=400,
            detail="Must specify `n2NotifyCallbackUri` when n2InformationClass is selected",
        )
    subscription_id = str(uuid.uuid4())

    crud_subscriptions.create_subscription(
        db=db,
        subscription_data=ue_n1n2_info_subscription_create_data,
        subscription_id=subscription_id,
    )

    response.headers[
        "Location"
    ] = f"/{ue_context_id}/n1-n2-messages/subscriptions/{subscription_id}"
    return UeN1N2InfoSubscriptionCreatedData(
        n1n2NotifySubscriptionId=subscription_id,
    )


@router.delete(
    path="/{ue_context_id}/n1-n2-messages/subscriptions/{subscription_id}",
    status_code=204,
)
async def n1n2_message_unsubscribe(
    ue_context_id: str,
    subscription_id: str,
    db: Session = Depends(get_db),
):
    db_subscription = crud_subscriptions.get_subscription_by_id(
        db=db, subscription_id=subscription_id
    )

    if not db_subscription:
        raise HTTPException(
            status_code=400,
            detail=f"Did not find subscription for id {subscription_id}",
        )
    crud_subscriptions.delete_subscription_by_id(db=db, subscription_id=subscription_id)


def n1_message_notify(url: Uri, n1_message_notification: N1MessageNotification) -> None:
    requests.post(url=url, json=json.loads(n1_message_notification.json()))
