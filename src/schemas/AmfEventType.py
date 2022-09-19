# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.

from enum import Enum


class AmfEventType(Enum):
    location_report = "LOCATION_REPORT"
    presence_in_aoi_report = "PRESENCE_IN_AOI_REPORT"
    timezone_report = "TIMEZONE_REPORT"
    access_type_report = "ACCESS_TYPE_REPORT"
    registration_state_report = "REGISTRATION_STATE_REPORT"
    connectivity_state_report = "CONNECTIVITY_STATE_REPORT"
    reachability_report = "REACHABILITY_REPORT"
    subscribed_data_report = "SUBSCRIBED_DATA_REPORT"
    communication_failure_report = "COMMIUNICATION_FAILURE_REPORT"
    ues_in_area_report = "UES_IN_AREA_REPORT"
