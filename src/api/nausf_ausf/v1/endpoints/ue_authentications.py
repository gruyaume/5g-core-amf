# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.

from fastapi import APIRouter

router = APIRouter()


@router.get(
    path="/",
    status_code=201,
    response_model=dict,
)
async def placeholder():
    return {"a": "b"}
