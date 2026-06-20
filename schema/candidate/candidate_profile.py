from pydantic import BaseModel
import uuid
from typing import Optional, List
from domain.candidate_profile import PrefessionalSituationStatus


class CreateCandidateProfile(BaseModel):

    candidate_id : uuid.UUID
    experience_years : Optional[int] = 0
    professional_situation : PrefessionalSituationStatus = PrefessionalSituationStatus.UNEMPLOYED
    key_competences : Optional[List[str]]


class UpdateCandidateProfile(BaseModel):

    experience_years : Optional[int] = None
    professional_situation : Optional[PrefessionalSituationStatus] = None
    key_competences : Optional[List[str]] = None
    
