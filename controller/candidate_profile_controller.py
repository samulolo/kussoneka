import uuid

from fastapi import APIRouter, Depends, status

from controller.dependecies import get_candidate_profile_service
from schema.app_response import BaseResponse, success_response
from schema.candidate.candidate_profile import CreateCandidateProfile, UpdateCandidateProfile
from service.candidate_profile_service import CandidateProfileService


profile_controller = APIRouter(prefix='/api/v1/candidate-profile', tags=['Candidate profile'])


@profile_controller.get("/{candidate_id}", status_code=status.HTTP_200_OK, response_model=BaseResponse)
def get(candidate_id : uuid.UUID, candidate_profile_service : CandidateProfileService = Depends(get_candidate_profile_service)) -> BaseResponse:
    candidate_profile = candidate_profile_service.get_by_id(candidate_id)
    return success_response(
        data=candidate_profile.model_dump(mode="json"),
        message="Perfil do candidato encontrado com sucesso"
    )


@profile_controller.post("/", status_code=status.HTTP_201_CREATED, response_model=BaseResponse)
def create(candidate_profile_create : CreateCandidateProfile, candidate_profile_service : CandidateProfileService = Depends(get_candidate_profile_service)) -> BaseResponse:
    candidate_profile = candidate_profile_service.create(candidate_profile_create)
    return success_response(
        status_code=status.HTTP_201_CREATED,
        data=candidate_profile.model_dump(mode="json"),
        message="Perfil do candidato criado com sucesso"
    )


@profile_controller.put("/{candidate_id}", status_code=status.HTTP_200_OK, response_model=BaseResponse)
def update(candidate_id : uuid.UUID, candidate_profile_update : UpdateCandidateProfile, candidate_profile_service : CandidateProfileService = Depends(get_candidate_profile_service)) -> BaseResponse:
    candidate_profile = candidate_profile_service.update(candidate_id, candidate_profile_update)
    return success_response(
        data=candidate_profile.model_dump(mode="json"),
        message="Perfil do candidato atualizado com sucesso"
    )


@profile_controller.delete("/{candidate_id}", status_code=status.HTTP_200_OK, response_model=BaseResponse)
def delete(candidate_id : uuid.UUID, candidate_profile_service : CandidateProfileService = Depends(get_candidate_profile_service)) -> BaseResponse:
    candidate_profile_service.delete(candidate_id)
    return success_response(message="Perfil do candidato removido com sucesso")
