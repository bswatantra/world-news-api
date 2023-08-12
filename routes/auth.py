from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session
import database

router = APIRouter(
    prefix="/login",
    tags=["Authentication"],
    responses={404: {"description": "Not found"}},
)

get_db = database.get_db


@router.post('/', status_code=status.HTTP_200_OK)
def login():
    return 'auth route'
