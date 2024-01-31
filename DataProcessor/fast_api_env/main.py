from fastapi import FastAPI
from .connection.rabbitmq import initialize_rabbitmq, close_rabbitmq_connection
from .controllers.controllers import router

app = FastAPI()
app.include_router(router)


@app.on_event("startup")
async def startup_event():
    initialize_rabbitmq()


@app.on_event("shutdown")
def shutdown_event():
    close_rabbitmq_connection()
