from typing import Union
from crewai.agent import Agent
from crewai.crew import Crew
from crewai.process import Process
from crewai.task import Task
from fastapi import FastAPI
from typing import Optional
from sqlmodel import Field, SQLModel

import uvicorn

class AgentInDB(SQLModel, table = True):
    id: Optional[int] = Field(default=None, primary_key=True)
    role: str


app = FastAPI()

@app.get("/")
def home():
    return {"Hello": "CrewAI"}

@app.post("agent/add")
def add_agent():
    pass

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

def run():
     uvicorn.run(app, host="0.0.0.0", port=8000)

