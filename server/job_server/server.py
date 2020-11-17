import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
import random
from typing import List
from prometheus_fastapi_instrumentator import Instrumentator


app = FastAPI()
Instrumentator().instrument(app).expose(app)

CHARACTERS = ['Darth Vader', 
              'Yoda',
              'Princess Leia',
              'Boba Fett',
              'Luke Skywalker',
              'Han Solo',
              'Obi-Wan Kenobi',
              'Nien Nunb', 
              'Wicket W. Warrick']

class CharacterID(BaseModel):
    id: int

class Characters(BaseModel):
    names: List[str]
    ids: List[int]

class Worktime(BaseModel):
    worktime: int
    name: str


@app.get("/")
def root():
    return "Job server running"

@app.get("/characters", response_model=Characters)
def get_characters():
    indicies = random.sample(range(0, len(CHARACTERS)), 3)
    return {"names":[CHARACTERS[idx] for idx in indicies], "ids":indicies}

@app.post("/worktime", response_model=Worktime)
def character_worktime(character: CharacterID):

    return {'worktime': len(CHARACTERS[character.id]), 'name': CHARACTERS[character.id]}



