# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.

from fiveg_core_common_schemas.SupportedFeatures import SupportedFeatures
from pydantic import BaseModel


class UeN1N2InfoSubscriptionCreatedData(BaseModel):
    n1n2NotifySubscriptionId: str
    supportedFeatures: SupportedFeatures = None
