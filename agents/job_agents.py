import os
from crewai import Agent

os.environ.get("OPENAI_API_KEY")

# Create an agent with a role and a goal
agent = Agent(
  role='Recruitment Score Agent',
  goal='Score the match between one candidate and jobs',
  verbose=True,
  backstory="You're an independent recruitment agent."
            "Your life depends on scoring the fit between candidates and jobs"
            "accurately."
)

# Create a second agent with the role of application filler
agent2 = Agent(
  role='Application Filler',
  goal='Fill applications to get a job',
  verbose=True,
  backstory="You're an independent job application filler."
            "Your life depends on filling applications in the name of candidates."
            "You are only paid if the candidate gets the job."
            "You are paid more if the candidate gets a higher salary."
            "The candidate is a good friend of yours in financial trouble and needs this job."
            "You are a good friend of the candidate is a great professional."
)
