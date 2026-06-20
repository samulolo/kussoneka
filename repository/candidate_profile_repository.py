from sqlmodel import Session, select
from domain.candidate_profile import CandidateProfile
import uuid


class CandidateProfileRepository:

    def __init__(self, session_db : Session):
        self.db = session_db

    
    def get_by_id(self, candidate_id : uuid.UUID):
        return self.db.get(CandidateProfile, candidate_id)

    def get_by_candidate_id(self, candidate_id : uuid.UUID):
        return self.db.exec(select(CandidateProfile).where(CandidateProfile.candidate_id == candidate_id)).first()

    def save(self, candidate_profile : CandidateProfile) -> CandidateProfile:

        self.db.add(candidate_profile)
        self.db.commit()
        self.db.refresh(candidate_profile)

        return candidate_profile

    def delete(self, candidate_profile : CandidateProfile):
        self.db.delete(candidate_profile)
        self.db.commit()
