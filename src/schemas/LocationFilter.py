# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.

from enum import Enum


class LocationFilter(Enum):
    tai = "TAI"
    cell_id = "CELL_ID"
    n3iwf = "N3IWF"
    ue_ip = "UE_IP"
    udp_port = "UDP_PORT"
