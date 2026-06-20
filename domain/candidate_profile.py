from sqlmodel import SQLModel, Field, Relationship, ARRAY, String
from typing import List, Optional
import uuid
from enum import Enum
from datetime import datetime, timezone


class PrefessionalSituationStatus(Enum):

    EMPLOYED = 'employed'
    UNEMPLOYED = 'unempoyed'


class CandidateProfile(SQLModel, table = True):

    __tablename__ = 'candidates_profile'

    candidate_id : uuid.UUID = Field(primary_key=True, foreign_key='candidates.id', nullable=False, unique=True)
    experience_years : int = Field(nullable=True, max_digits=3)
    # Vou assumir que por padrão o candidato está desempregado
    professional_situation : PrefessionalSituationStatus  = Field(default=PrefessionalSituationStatus.UNEMPLOYED, nullable=True)
    key_competences : Optional[List[str]] = Field(nullable=True, sa_type=ARRAY(String))
    created_at : datetime = Field(default_factory=lambda : datetime.now(timezone.utc))
    updated_at : datetime = Field(default_factory=lambda : datetime.now(timezone.utc))

    candidate : Optional['Candidate'] = Relationship(back_populates='professiona_profile')
