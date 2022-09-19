# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.

from fiveg_core_common_schemas.PresenceState import PresenceState
from pydantic import BaseModel


class LadnInfo(BaseModel):
    ladn: str
    presence: PresenceState = None
