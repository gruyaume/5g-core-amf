# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.

from sqlalchemy import Column, String

from database.base_class import Base


class SubscriptionData(Base):
    __tablename__ = "subscription_data"
    id = Column(String, primary_key=True, index=True)
    n2InformationClass = Column(String, index=True)
    n2NotifyCallbackUri = Column(String, index=True)
    n1MessageClass = Column(String, index=True)
    n1NotifyCallbackUri = Column(String, index=True)
    nfId = Column(String, index=True)
    supportedFeatures = Column(String, index=True)
