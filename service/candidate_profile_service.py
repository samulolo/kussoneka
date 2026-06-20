import uuid
from datetime import datetime, timezone

from domain.candidate_profile import CandidateProfile
from exception.app_exceptions import ResouceAlreadyExist, ResourceNotFound
from repository.candidate_profile_repository import CandidateProfileRepository
from schema.candidate.candidate_profile import CreateCandidateProfile, UpdateCandidateProfile


class CandidateProfileService:

    def __init__(self, candidate_profile_repository : CandidateProfileRepository):
        self.candidate_profile_repository = candidate_profile_repository

    def _ensure_candidate_profile_exists(self, candidate_id : uuid.UUID):

        exist_candidate_profile = self.candidate_profile_repository.get_by_candidate_id(candidate_id)

        if not exist_candidate_profile:
            return False
        
        return exist_candidate_profile

    def get_by_id(self, candidate_id : uuid.UUID):

        candidate_profile = self._ensure_candidate_profile_exists.get_by_id(candidate_id)

        if not candidate_profile:
            raise ResourceNotFound("Perfil do candidato não encontrado")

        return candidate_profile

    def create(self, candidate_profile_create : CreateCandidateProfile):

        if self._ensure_candidate_profile_exists(candidate_profile_create.candidate_id):
            raise ResouceAlreadyExist("Já existe um perfil para esse candidato")

        new_candidate_profile = CandidateProfile(**candidate_profile_create.model_dump())

        return self.candidate_profile_repository.save(new_candidate_profile)

    def update(self, candidate_id : uuid.UUID, candidate_profile_update : UpdateCandidateProfile):

        candidate_profile = self.candidate_profile_repository.get_by_id(candidate_id)

        if not candidate_profile:
            raise ResourceNotFound("Perfil do candidato não encontrado")

        update_data = candidate_profile_update.model_dump(exclude_unset=True)

        for field, value in update_data.items():
            setattr(candidate_profile, field, value)

        candidate_profile.updated_at = datetime.now(timezone.utc)

        return self.candidate_profile_repository.save(candidate_profile)

    def delete(self, candidate_id : uuid.UUID):

        candidate_profile = self.candidate_profile_repository.get_by_id(candidate_id)

        if not candidate_profile:
            raise ResourceNotFound("Perfil do candidato não encontrado")

        self.candidate_profile_repository.delete(candidate_profile)
