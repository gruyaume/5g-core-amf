# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.

from enum import Enum


class SmsSupport(Enum):
    threegpp = "3GPP"
    non_threegpp = "NON_3GPP"
    both = "BOTH"
    none = "NONE"
