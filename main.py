from fastapi import FastAPI
import uvicorn
from controller.candidate_controller import candidate_controller

app = FastAPI(
    title="kussoneka",
    version="1.0")


routes = [

    candidate_controller
]

for controller in routes:
    app.include_router(controller)





if __name__ == '__main__':
    uvicorn.run()