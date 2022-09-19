# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.

from fiveg_core_common_schemas.N1MessageClass import N1MessageClass
from fiveg_core_common_schemas.N2InformationClass import N2InformationClass
from fiveg_core_common_schemas.NfInstanceId import NfInstanceId
from fiveg_core_common_schemas.SupportedFeatures import SupportedFeatures
from fiveg_core_common_schemas.Uri import Uri
from pydantic import BaseModel


class UeN1N2InfoSubscriptionCreateData(BaseModel):
    n2InformationClass: N2InformationClass = None
    n2NotifyCallbackUri: Uri = None
    n1MessageClass: N1MessageClass = None
    n1NotifyCallbackUri: Uri = None
    nfId: NfInstanceId = None
    supportedFeatures: SupportedFeatures = None
