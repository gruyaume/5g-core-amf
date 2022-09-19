# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.

from fiveg_core_common_schemas.Snssai import Snssai
from pydantic import BaseModel


class NssaiMapping(BaseModel):
    mappedSnssai: Snssai
    hSnssai: Snssai
