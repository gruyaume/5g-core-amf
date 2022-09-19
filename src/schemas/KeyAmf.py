# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.

from pydantic import BaseModel

from schemas.KeyAmfType import KeyAmfType


class KeyAmf(BaseModel):
    keyType: KeyAmfType
    keyVal: str
