# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.

from fiveg_core_common_schemas.N1MessageClass import N1MessageClass
from fiveg_core_common_schemas.NfInstanceId import NfInstanceId
from pydantic import BaseModel

from schemas.RefToBinaryData import RefToBinaryData


class N1MessageContainer(BaseModel):
    n1MessageClass: N1MessageClass
    n1MessageContent: RefToBinaryData
    nfId: NfInstanceId = None
