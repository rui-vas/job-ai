import os 

from crewai import Agent, Process, Crew

os.environ.get("OPENAI_API_KEY")

agent1 = Agent(
    role="",
    goal="",
    backstory="",
    verbose=True,
    allow_delegation=True
)

agent2 = Agent(
    role="",
    goal="",
    backstory="",
    verbose=True,
    allow_delegation=True
)

agent3 = Agent(
    role="",
    goal="",
    backstory="",
    verbose=True,
    allow_delegation=True
)