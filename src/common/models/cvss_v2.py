# generated by datamodel-codegen:
#   filename:  https://csrc.nist.gov/schema/nvd/api/2.0/external/cvss-v2.0.json
#   timestamp: 2023-03-02T09:56:35+00:00

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field, confloat, constr


class Version(Enum):
    """
    CVSS Version
    """

    field_2_0 = '2.0'


class AccessVectorType(Enum):
    NETWORK = 'NETWORK'
    ADJACENT_NETWORK = 'ADJACENT_NETWORK'
    LOCAL = 'LOCAL'


class AccessComplexityType(Enum):
    HIGH = 'HIGH'
    MEDIUM = 'MEDIUM'
    LOW = 'LOW'


class AuthenticationType(Enum):
    MULTIPLE = 'MULTIPLE'
    SINGLE = 'SINGLE'
    NONE = 'NONE'


class CiaType(Enum):
    NONE = 'NONE'
    PARTIAL = 'PARTIAL'
    COMPLETE = 'COMPLETE'


class ExploitabilityType(Enum):
    UNPROVEN = 'UNPROVEN'
    PROOF_OF_CONCEPT = 'PROOF_OF_CONCEPT'
    FUNCTIONAL = 'FUNCTIONAL'
    HIGH = 'HIGH'
    NOT_DEFINED = 'NOT_DEFINED'


class RemediationLevelType(Enum):
    OFFICIAL_FIX = 'OFFICIAL_FIX'
    TEMPORARY_FIX = 'TEMPORARY_FIX'
    WORKAROUND = 'WORKAROUND'
    UNAVAILABLE = 'UNAVAILABLE'
    NOT_DEFINED = 'NOT_DEFINED'


class ReportConfidenceType(Enum):
    UNCONFIRMED = 'UNCONFIRMED'
    UNCORROBORATED = 'UNCORROBORATED'
    CONFIRMED = 'CONFIRMED'
    NOT_DEFINED = 'NOT_DEFINED'


class CollateralDamagePotentialType(Enum):
    NONE = 'NONE'
    LOW = 'LOW'
    LOW_MEDIUM = 'LOW_MEDIUM'
    MEDIUM_HIGH = 'MEDIUM_HIGH'
    HIGH = 'HIGH'
    NOT_DEFINED = 'NOT_DEFINED'


class TargetDistributionType(Enum):
    NONE = 'NONE'
    LOW = 'LOW'
    MEDIUM = 'MEDIUM'
    HIGH = 'HIGH'
    NOT_DEFINED = 'NOT_DEFINED'


class CiaRequirementType(Enum):
    LOW = 'LOW'
    MEDIUM = 'MEDIUM'
    HIGH = 'HIGH'
    NOT_DEFINED = 'NOT_DEFINED'


class CveCvssDataModel(BaseModel):
    version: Version = Field(..., description='CVSS Version')
    vectorString: constr(
        regex=r'^((AV:[NAL]|AC:[LMH]|Au:[MSN]|[CIA]:[NPC]|E:(U|POC|F|H|ND)|RL:(OF|TF|W|U|ND)|RC:(UC|UR|C|ND)|CDP:(N|L|LM|MH|H|ND)|TD:(N|L|M|H|ND)|[CIA]R:(L|M|H|ND))/)*(AV:[NAL]|AC:[LMH]|Au:[MSN]|[CIA]:[NPC]|E:(U|POC|F|H|ND)|RL:(OF|TF|W|U|ND)|RC:(UC|UR|C|ND)|CDP:(N|L|LM|MH|H|ND)|TD:(N|L|M|H|ND)|[CIA]R:(L|M|H|ND))$'
    )
    accessVector: Optional[AccessVectorType] = None
    accessComplexity: Optional[AccessComplexityType] = None
    authentication: Optional[AuthenticationType] = None
    confidentialityImpact: Optional[CiaType] = None
    integrityImpact: Optional[CiaType] = None
    availabilityImpact: Optional[CiaType] = None
    baseScore: confloat(ge=0.0, le=10.0)
    exploitability: Optional[ExploitabilityType] = None
    remediationLevel: Optional[RemediationLevelType] = None
    reportConfidence: Optional[ReportConfidenceType] = None
    temporalScore: Optional[confloat(ge=0.0, le=10.0)] = None
    collateralDamagePotential: Optional[CollateralDamagePotentialType] = None
    targetDistribution: Optional[TargetDistributionType] = None
    confidentialityRequirements: Optional[CiaRequirementType] = None
    integrityRequirements: Optional[CiaRequirementType] = None
    availabilityRequirements: Optional[CiaRequirementType] = None
    environmentalScore: Optional[confloat(ge=0.0, le=10.0)] = None
