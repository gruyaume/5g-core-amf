# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.

from fiveg_core_common_schemas.PresenceInfo import PresenceInfo
from pydantic import BaseModel

from schemas.LadnInfo import LadnInfo


class AmfEventArea(BaseModel):
    presenceInfo: PresenceInfo
    ladnInfo: LadnInfo
