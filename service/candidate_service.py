import uuid

from schema.candidate.candiatate import CandidateCreate, CandidateUpdate
from domain.candidate import Candidate
from repository.candidate_repository import CandidateRepository
from exception.app_exceptions import ResouceAlreadyExist, ResourceNotFound

class CandidateService:


    def __init__(self, candidtae_repository : CandidateRepository):
        self.candidate_repository = candidtae_repository


    def _ensure_user_exits(self, email : str):

        exist_candidate = self.candidate_repository.get_by_email(email)
        if not exist_candidate:
            return False
        return True


    def create(self, candidate_create : CandidateCreate):

        if  self._ensure_user_exits(candidate_create.email):
            raise ResouceAlreadyExist("Já existe uma conta com esse email")
        
        new_candidate = Candidate(**candidate_create.model_dump())
       
        return  self.candidate_repository.save(new_candidate)



    def update(self, candidate_id : uuid.UUID, candidate_update : CandidateUpdate):

        candidate = self.candidate_repository.get_by_id(candidate_id)

        if not candidate:
            raise ResourceNotFound("Candidato não encontrado")

        update_data = candidate_update.model_dump(exclude_unset=True)

        if "email" in update_data:
            exist_candidate = self.candidate_repository.get_by_email(update_data["email"])
            if exist_candidate and exist_candidate.id != candidate.id:
                raise ResouceAlreadyExist("Já existe uma conta com esse email")

        for field, value in update_data.items():
            setattr(candidate, field, value)

        return self.candidate_repository.save(candidate)


    def delete(self, candidate_id : uuid.UUID):

        candidate = self.candidate_repository.get_by_id(candidate_id)

        if not candidate:
            raise ResourceNotFound("Candidato não encontrado")

        self.candidate_repository.delete(candidate)
