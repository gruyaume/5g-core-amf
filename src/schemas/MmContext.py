# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.

from typing import List

from fiveg_core_common_schemas.AccessType import AccessType
from fiveg_core_common_schemas.NsiId import NsiId
from fiveg_core_common_schemas.Snssai import Snssai
from pydantic import BaseModel

from schemas.ExpectedUeBehavior import ExpectedUeBehavior
from schemas.NasCount import NasCount
from schemas.NasSecurityMode import NasSecurityMode
from schemas.NssaiMapping import NssaiMapping
from schemas.S1UeNetworkCapability import S1UeNetworkCapability
from schemas.UeSecurityCapability import UeSecurityCapability


class MmContext(BaseModel):
    accessType: AccessType
    nasSecurityMode: NasSecurityMode = None
    nasDownlinkCount: NasCount = None
    nasUplinkCount: NasCount = None
    ueSecurityCapability: UeSecurityCapability = None
    s1UeNetworkCapability: S1UeNetworkCapability = None
    allowedNssaiList: List[Snssai] = None
    nssaiMappingList: List[NssaiMapping] = None
    nsInstanceList: List[NsiId] = None
    expectedUEbehavior: ExpectedUeBehavior = None
