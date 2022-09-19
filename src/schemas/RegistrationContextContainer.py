# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.

from typing import List

from fiveg_core_common_schemas.AccessType import AccessType
from fiveg_core_common_schemas.AllowedNssai import AllowedNssai
from fiveg_core_common_schemas.ConfiguredSnssai import ConfiguredSnssai
from fiveg_core_common_schemas.Ipv4Addr import Ipv4Addr
from fiveg_core_common_schemas.Ipv6Addr import Ipv6Addr
from fiveg_core_common_schemas.NgRanIdentifier import NgRanIdentifier
from fiveg_core_common_schemas.Snssai import Snssai
from fiveg_core_common_schemas.TimeZone import TimeZone
from pydantic import BaseModel

from schemas.UeContext import UeContext


class RegistrationContextContainer(BaseModel):
    ueContext: UeContext
    localTimeZone: TimeZone = None
    anType: AccessType
    anN2ApId: int
    ranNodeId: NgRanIdentifier
    anN2IPv4Addr: Ipv4Addr = None
    anN2IPv6Addr: Ipv6Addr = None
    allowedNssai: AllowedNssai = None
    configuredNssai: List[ConfiguredSnssai] = None
    rejectedNssaiInPlmn: List[Snssai] = None
    rejectedNssaiInTa: List[Snssai] = None
