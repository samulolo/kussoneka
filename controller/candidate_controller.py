import uuid

from fastapi import APIRouter, status, Depends
from schema.candidate.candiatate import CandidateCreate, CandidateUpdate
from service.candidate_service import CandidateService
from controller.dependecies import get_candidate_service
from schema.app_response import BaseResponse, success_response


candidate_controller = APIRouter(prefix='/api/v1/candidate', tags=['candidate'])



@candidate_controller.get("/", status_code=status.HTTP_200_OK)
def get() -> BaseResponse:
    return success_response(message="It's going to be fine")


@candidate_controller.post("/", status_code=status.HTTP_201_CREATED, response_model=BaseResponse)
def create(candicate_create : CandidateCreate, candidate_service :CandidateService = Depends(get_candidate_service)) -> BaseResponse: 
    candidate = candidate_service.create(candicate_create)
    return success_response(
        status_code=status.HTTP_201_CREATED,
        data=candidate.model_dump(mode="json"),
        message="Candidato criado com sucesso"
    )


@candidate_controller.put("/{candidate_id}", status_code=status.HTTP_200_OK, response_model=BaseResponse)
def update(candidate_id : uuid.UUID, candidate_update : CandidateUpdate, candidate_service :CandidateService = Depends(get_candidate_service)) -> BaseResponse:
    candidate = candidate_service.update(candidate_id, candidate_update)
    return success_response(
        data=candidate.model_dump(mode="json"),
        message="Candidato atualizado com sucesso"
    )


@candidate_controller.delete("/{candidate_id}", status_code=status.HTTP_200_OK, response_model=BaseResponse)
def delete(candidate_id : uuid.UUID, candidate_service :CandidateService = Depends(get_candidate_service)) -> BaseResponse:
    candidate_service.delete(candidate_id)
    return success_response(message="Candidato removido com sucesso")
