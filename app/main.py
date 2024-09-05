from fastapi import FastAPI
from routers import task, user


app = FastAPI()


@app.get('/')
async def welcome():
    return {'message': 'Welcome to Taskmanager'}

app.include_router(task.task_router)
app.include_router(user.user_router)