# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.

from fiveg_core_common_schemas.Uinteger import Uinteger
from pydantic import BaseModel

from schemas.KeyAmf import KeyAmf
from schemas.NgKsi import NgKsi


class SeafData(BaseModel):
    ngKsi: NgKsi
    keyAmf: KeyAmf
    nh: str = None
    ncc: Uinteger = None
    keyAmfChangeInd: bool = None
