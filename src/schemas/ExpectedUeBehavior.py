# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.

from fiveg_core_common_schemas.DateTime import DateTime
from fiveg_core_common_schemas.UserLocation import UserLocation
from pydantic import BaseModel


class ExpectedUeBehavior(BaseModel):
    expMoveTrajectory: UserLocation
    validityTime: DateTime
