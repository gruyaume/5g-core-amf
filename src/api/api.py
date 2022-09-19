# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.

from fastapi import APIRouter

from api.namf_comm.v1.endpoints import ue_contexts
from database.session import engine
from models import SubscriptionData

SubscriptionData.Base.metadata.create_all(bind=engine)  # TODO: Replace with db migrations.

api_router = APIRouter()
api_router.include_router(
    ue_contexts.router,
    prefix="/namf-comm/v1/ue-contexts",
)
