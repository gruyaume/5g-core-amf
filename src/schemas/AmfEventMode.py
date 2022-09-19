# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.

from fiveg_core_common_schemas.DateTime import DateTime
from pydantic import BaseModel

from schemas.AmfEventTrigger import AmfEventTrigger


class AmfEventMode(BaseModel):
    trigger: AmfEventTrigger
    maxReports: int = None
    expiry: DateTime = None
