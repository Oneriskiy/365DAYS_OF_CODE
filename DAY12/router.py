from fastapi import APIRouter, HTTPException
from data import monuments, users
from models import MonumentsSchema


router = APIRouter()

@router.get("/monuments",
         summary='get_monuments',
         description='returns all monuments',
         tags=['monuments', 'get'])
def get_monuments():
    if not monuments:
        raise HTTPException(status_code=404, detail='Not Found')
    return monuments


@router.post("/monuments",
          summary='post_monuments',
          description='add new monument',
          tags=['monuments', 'post'])
def post_monuments(monument: MonumentsSchema):
    monuments[monument.title] = monument.price
    return {'message': 'ok'}


@router.post("/monuments/register")
def register():
    pass