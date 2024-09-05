from fastapi import APIRouter


task_router = APIRouter(prefix='/task', tags=['task'])


@task_router.get('/')
async def all_tasks():
    pass


@task_router.get('/task_id')
async def task_by_id():
    pass


@task_router.post('/create')
async def create_task():
    pass


@task_router.put('/upgrade')
async def upgrade_task():
    pass


@task_router.delete('/delete')
async def delete_task():
    pass