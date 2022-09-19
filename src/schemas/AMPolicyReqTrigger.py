# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.

from enum import Enum


class AMPolicyReqTrigger(Enum):
    location_changed = "LOCATION_CHANGE"
    pra_change = "PRA_CHANGE"
    sari_change = "SARI_CHANGE"
    rfsp_index_change = "RFSP_INDEX_CHANGE"
