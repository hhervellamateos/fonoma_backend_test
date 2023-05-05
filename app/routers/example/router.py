from fastapi import APIRouter
from routers.example import controller

router = APIRouter(prefix='')

router.add_api_route(
    path="/",
    endpoint=controller.hello_world,
    methods=["GET"],
)