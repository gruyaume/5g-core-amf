# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.

from fiveg_core_common_schemas.Uinteger import Uinteger
from pydantic import BaseModel

from schemas.ScType import ScType


class NgKsi(BaseModel):
    tsc: ScType
    ksi: Uinteger
