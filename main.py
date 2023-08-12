from fastapi import FastAPI, status, Response, Depends, HTTPException
from database import Base, engine
from routes import auth, news

from dotenv import load_dotenv

app = FastAPI()

load_dotenv()

Base.metadata.create_all(engine)
app.include_router(auth.router)
app.include_router(news.router)
