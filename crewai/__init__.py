from crewai.agent import Agent
from crewai.crew import Crew
from crewai.process import Process
from crewai.task import Task

import uvicorn
if __name__ == "__main__":
     uvicorn.run("api:app", host="0.0.0.0", port=8000, reload=True)