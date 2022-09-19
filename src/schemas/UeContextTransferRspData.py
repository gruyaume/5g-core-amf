# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.

from fiveg_core_common_schemas.SupportedFeatures import SupportedFeatures
from pydantic import BaseModel

from schemas.UeContext import UeContext


class UeContextTransferRspData(BaseModel):
    ueContext: UeContext
    supportedFeatures: SupportedFeatures = None
