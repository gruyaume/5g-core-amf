# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.

from typing import List

from fiveg_core_common_schemas.Ambr import Ambr
from fiveg_core_common_schemas.Area import Area
from fiveg_core_common_schemas.CoreNetworkType import CoreNetworkType
from fiveg_core_common_schemas.Gpsi import Gpsi
from fiveg_core_common_schemas.GroupId import GroupId
from fiveg_core_common_schemas.NfInstanceId import NfInstanceId
from fiveg_core_common_schemas.Pei import Pei
from fiveg_core_common_schemas.RatType import RatType
from fiveg_core_common_schemas.ServiceAreaRestriction import ServiceAreaRestriction
from fiveg_core_common_schemas.Supi import Supi
from fiveg_core_common_schemas.TraceData import TraceData
from fiveg_core_common_schemas.Uri import Uri
from pydantic import BaseModel

from schemas.AmfEventSubscription import AmfEventSubscription
from schemas.AMPolicyReqTrigger import AMPolicyReqTrigger
from schemas.DrxParameter import DrxParameter
from schemas.FivegmmCapability import FivegmmCapability
from schemas.MmContext import MmContext
from schemas.PduSessionContext import PduSessionContext
from schemas.RfspIndex import RfspIndex
from schemas.SeafData import SeafData
from schemas.SmsSupport import SmsSupport


class UeContext(BaseModel):
    supi: Supi = None
    supiUnauthInd: bool = None
    gpsiList: List[Gpsi] = None
    pei: Pei = None
    groupList: List[GroupId] = None
    drxParameter: DrxParameter = None
    subRfsp: RfspIndex = None
    usedRfsp: RfspIndex = None
    subUeAmbr: Ambr = None
    smsSupport: SmsSupport
    smsfId: NfInstanceId = None
    seafData: SeafData = None
    fivegmmCapability: FivegmmCapability = None
    pcfId: NfInstanceId = None
    pcfAmPolicyUri: Uri = None
    amPolicyReqTriggerList: List[AMPolicyReqTrigger] = None
    hpcfId: NfInstanceId = None
    restrictedRatList: List[RatType] = None
    forbiddenAreaList: List[Area] = None
    serviceAreaRestriction: ServiceAreaRestriction = None
    restrictedCnList: List[CoreNetworkType] = None
    eventSubscriptionList: List[AmfEventSubscription] = None
    mmContextList: List[MmContext] = None
    sessionContextList: List[PduSessionContext] = None
    traceData: TraceData = None
