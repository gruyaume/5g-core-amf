# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.

from fastapi import APIRouter

from api.nausf_ausf.v1.endpoints import ue_authentications

api_router = APIRouter()
api_router.include_router(
    ue_authentications.router,
    prefix="/nausf-ausf/v1/ue-authentications",
)
