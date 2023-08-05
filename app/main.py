from fastapi import FastAPI
# from random import randrange
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from . import models, schemas, utils
from sqlalchemy.orm import Session
from .database import engine
from .routers import post, user, auth, vote

#models.Base.metadata.create_all(bind=engine)

origins = ["*"]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# my_posts = [{"id": 1, "title": "Favourite Places in Lahore", "content": "I love Badshahi Mosque"}, {"id": 2, "title": "Favorite Foods", "content": "I like Lapeta Burger"}]

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}




