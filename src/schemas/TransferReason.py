# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.

from enum import Enum


class TransferReason(Enum):
    init_reg = "INIT_REG"
    mobi_reg = "MOBI_REG"
    mobi_reg_ue_validated = "MOBI_REG_UE_VALIDATED"
