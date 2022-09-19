# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.

from enum import Enum


class N2InformationClass(Enum):
    SM = "SM"
    NRPPa = "NRPPa"
    PWS = "PWS"
    PWS_BCAL = "PWS-BCAL"
    PWS_RF = "PWS-RF"
