from fastapi import APIRouter
from ..
router = APIRouter(
    prefix="/models",
    tags=["models"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def about():
    return "Здесь собраны методы для вызова моделей обработки данных"



@router.get("/sum")
def sum(x: float= 0, y: float=0):
    return my_sum(x, y)