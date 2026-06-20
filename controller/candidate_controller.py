from fastapi import APIRouter



candidate_controller = APIRouter(prefix='/api/v1/candidate', tags=['candidate'])



@candidate_controller.get("/")
def get():
    return "It's going to be fine"