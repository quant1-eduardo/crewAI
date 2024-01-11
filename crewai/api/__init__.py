from typing import Union
from crewai.agent import Agent
from crewai.crew import Crew
from crewai.process import Process
from crewai.task import Task
from fastapi import FastAPI
from typing import Optional
from sqlmodel import Field, SQLModel, Session, create_engine, select
from pydantic import ConfigDict

import uvicorn


class Table():
    def add(obj):
        with Session(engine) as session:
            session.add(obj)
            session.commit()

    def list_all (class_ref):
        with Session(engine) as session:
            statement = select(class_ref)
            return [value for value in session.exec(statement)]

class Agents(SQLModel, table = True):
    id : Optional[int] = Field(default=None, primary_key=True)
    role: str
    goal: str
    backstory: str
    llm: str
    memory: str
    verbose: bool
    allow_delegation: bool
    tools: str
    agent_executor : str
    tools_handle : str
    cache_handler: str

    def list_all( ):
        return Table.list_all(Agents)
    

app = FastAPI()


engine = create_engine("sqlite:///database.db")
SQLModel.metadata.create_all(engine)

'''
ag1 = Agents(role= "Teste", goal = "Cozinhar", backstory = ' ',
    llm = '',
    memory = '200MB',
    verbose = True,
    allow_delegation = True,
    tools = '',
    agent_executor = '',
    tools_handle = '',
    cache_handler = '')

Table.add(ag1)
'''

#print( Agent.__dict__["model_fields"].keys() )
#print( Agent.__dict__["model_fields"]["id"] )
#print( Agent.__dict__["model_fields"]["backstory"] )
#print(Agent.__dict__["__pydantic_core_schema__"].keys())
#print("\n\n")
#print(Agent.__class__.__dict__)
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