from repository.candidate_repository import CandidateRepository
from repository.candidate_profile_repository import CandidateProfileRepository
from service.candidate_service import CandidateService
from service.candidate_profile_service import CandidateProfileService
from database import session_db



def get_candidate_service(session : session_db):
    return CandidateService(candidtae_repository=CandidateRepository(session))


def get_candidate_profile_service(session : session_db):
    return CandidateProfileService(candidate_profile_repository=CandidateProfileRepository(session))
