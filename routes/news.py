import httpx
from fastapi import APIRouter
import database
import requests
import os


router = APIRouter(
    prefix="/news",
    tags=["News"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

get_db = database.get_db


@router.get("/")
def news():
    try:
        response = requests.get(
            os.getenv("WORLD_NEWS_API")+'?' +
            'api-key' + '='+os.getenv("WORLD_NEWS_API_KEY")
        )
        response.raise_for_status()
        return response.json()
    except httpx.RequestError as e:
        return {"error": "Request to third-party API failed"}
    except httpx.HTTPStatusError as e:
        return {"error": "Third-party API returned an error status"}
