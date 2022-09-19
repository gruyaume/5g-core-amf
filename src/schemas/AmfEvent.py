# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.

from typing import List

from pydantic import BaseModel

from schemas.AmfEventArea import AmfEventArea
from schemas.AmfEventType import AmfEventType
from schemas.LocationFilter import LocationFilter
from schemas.SubscribedDataFilter import SubscribedDataFilter


class AmfEvent(BaseModel):
    type: AmfEventType
    immediateFlag: bool = None
    areaList: List[AmfEventArea] = None
    locationFilterList: List[LocationFilter] = None
    subscribedDataFilterList: List[SubscribedDataFilter] = None
