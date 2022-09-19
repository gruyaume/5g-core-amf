# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.

from fiveg_core_common_schemas.CorrelationID import CorrelationID
from pydantic import BaseModel

from schemas.N1MessageContainer import N1MessageContainer
from schemas.RegistrationContextContainer import RegistrationContextContainer


class N1MessageNotification(BaseModel):
    n1NotifySubscriptionId: str = None
    n1MessageContainer: N1MessageContainer
    IcsCorrelationId: CorrelationID = None
    registrationCtxtContainer: RegistrationContextContainer = None
