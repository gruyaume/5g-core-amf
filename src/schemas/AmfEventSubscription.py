# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.

from typing import List

from fiveg_core_common_schemas.Gpsi import Gpsi
from fiveg_core_common_schemas.GroupId import GroupId
from fiveg_core_common_schemas.NfInstanceId import NfInstanceId
from fiveg_core_common_schemas.Pei import Pei
from fiveg_core_common_schemas.Supi import Supi
from fiveg_core_common_schemas.Uri import Uri
from pydantic import BaseModel

from schemas.AmfEvent import AmfEvent
from schemas.AmfEventMode import AmfEventMode


class AmfEventSubscription(BaseModel):
    eventList: List[AmfEvent]
    notifyUri: Uri
    notifyCorrelationId: str
    nfId: NfInstanceId
    subsChangeNotifyUri: Uri = None
    subsChangeNotifyCorelationId: str = None
    supi: Supi = None
    groupId: GroupId = None
    gpsi: Gpsi = None
    pei: Pei = None
    anyUE: bool = None
    options: AmfEventMode = None
