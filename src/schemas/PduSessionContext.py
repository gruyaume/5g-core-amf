# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.

from typing import List

from fiveg_core_common_schemas.AccessType import AccessType
from fiveg_core_common_schemas.Dnn import Dnn
from fiveg_core_common_schemas.EbiArpMapping import EbiArpMapping
from fiveg_core_common_schemas.NfInstanceId import NfInstanceId
from fiveg_core_common_schemas.NsiId import NsiId
from fiveg_core_common_schemas.PduSessionId import PduSessionId
from fiveg_core_common_schemas.Snssai import Snssai
from fiveg_core_common_schemas.Uri import Uri
from pydantic import BaseModel


class PduSessionContext(BaseModel):
    pduSessionId: PduSessionId
    smContextRef: Uri
    sNssai: Snssai
    dnn: Dnn
    accessType: AccessType
    allocatedEbiList: List[EbiArpMapping]
    hsmfId: NfInstanceId = None
    vsmfId: NfInstanceId = None
    nsInstance: NsiId = None
