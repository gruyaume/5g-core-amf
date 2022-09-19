# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.

from pydantic import BaseModel

from schemas.CipheringAlgorithm import CipheringAlgorithm
from schemas.IntegrityAlgorithm import IntegrityAlgorithm


class NasSecurityMode(BaseModel):
    integrityAlgorithm: IntegrityAlgorithm
    cipheringAlgorithm: CipheringAlgorithm
