# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.

from typing import Optional

from fiveg_core_common_schemas.N1MessageClass import N1MessageClass
from sqlalchemy.orm import Session

from models.SubscriptionData import SubscriptionData
from schemas.N2InformationClass import N2InformationClass
from schemas.UeN1N2InfoSubscriptionCreateData import UeN1N2InfoSubscriptionCreateData


def create_subscription(
    db: Session,
    subscription_data: UeN1N2InfoSubscriptionCreateData,
    subscription_id: str,
) -> None:

    db_subscription = SubscriptionData(
        id=subscription_id,
        n2InformationClass=str(subscription_data.n2InformationClass.value)
        if subscription_data.n2InformationClass is not None
        else None,
        n2NotifyCallbackUri=subscription_data.n2NotifyCallbackUri,
        n1MessageClass=str(subscription_data.n1MessageClass.value)
        if subscription_data.n1MessageClass is not None
        else None,
        n1NotifyCallbackUri=subscription_data.n1NotifyCallbackUri,
        nfId=subscription_data.nfId,
        supportedFeatures=subscription_data.supportedFeatures,
    )
    db.add(db_subscription)
    db.commit()
    db.refresh(db_subscription)


def get_subscription_by_id(
    db: Session,
    subscription_id: str,
) -> Optional[UeN1N2InfoSubscriptionCreateData]:
    db_subscription = (
        db.query(SubscriptionData).filter(SubscriptionData.id == subscription_id).first()
    )
    if not db_subscription:
        return None

    return UeN1N2InfoSubscriptionCreateData(
        n2InformationClass=N2InformationClass(db_subscription.n2InformationClass)
        if db_subscription.n2InformationClass
        else None,
        n2NotifyCallbackUri=db_subscription.n2NotifyCallbackUri,
        n1MessageClass=N1MessageClass(db_subscription.n1MessageClass)
        if db_subscription.n1MessageClass
        else None,
        n1NotifyCallbackUri=db_subscription.n2NotifyCallbackUri,
        nfId=db_subscription.nfId,
        supportedFeatures=db_subscription.supportedFeatures,
    )


def delete_subscription_by_id(
    db: Session,
    subscription_id: str,
) -> None:
    db_subscription = (
        db.query(SubscriptionData).filter(SubscriptionData.id == subscription_id).first()
    )
    if not db_subscription:
        raise ValueError(f"Can't find subscription for ID {subscription_id}")
    db.delete(db_subscription)
    db.commit()
