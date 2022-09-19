# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.

from fiveg_core_common_schemas.SupportedFeatures import SupportedFeatures
from pydantic import BaseModel

from schemas.N1MessageContainer import N1MessageContainer
from schemas.TransferReason import TransferReason


class UeContextTransferReqData(BaseModel):
    reason: TransferReason
    regRequest: N1MessageContainer = None
    supportedFeatures: SupportedFeatures = None
