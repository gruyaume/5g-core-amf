# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.

from enum import Enum


class AmfEventTrigger(Enum):
    one_time = "ONE_TIME"
    continuous = "CONTINUOUS"
