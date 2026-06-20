from fastapi import FastAPI
import uvicorn
from controller.candidate_controller import candidate_controller
from controller.candidate_profile_controller import profile_controller
from database import create_table
from exception.global_exceptipns import global_exceptions

app = FastAPI(
    title="kussoneka",
    version="1.0")


create_table() # cria as tabelas da base de dados.
global_exceptions(app)

routes = [
    candidate_controller,
    profile_controller
]

for controller in routes:
    app.include_router(controller)





if __name__ == '__main__':
    uvicorn.run()
