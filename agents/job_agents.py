import os
from crewai import Agent, Task, Crew, Process

os.environ.get("OPENAI_API_KEY")

# AGENTS
# Create an agent with a role and a goal
score_agent = Agent(
  role='Recruitment Score Agent',
  goal='Score the match between one candidate and jobs',
  verbose=True,
  backstory="You're an independent recruitment agent."
            "Your life depends on scoring the fit between candidates and jobs"
            "accurately."
)

# Create a second agent with the role of application filler
application_agent = Agent(
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


# TASKS
# Create a task for the score agent to score the match between a candidate and one job based on the candidate's resume and job description
scoring_task = Task(
  description='Score the match between a candidate and a job based on the candidate\'s resume and job description',
  agent=score_agent
)

# Create a task for the application filler agent to fill an application for a candidate
application_task = Task(
  description='Fill an application for a candidate',
  agent=application_agent
)

# PROCESSES
# Instantiate crew
tech_crew = Crew(
  agents=[score_agent, application_agent],
  tasks=[scoring_task, application_task],
  process=Process.sequential  # Tasks will be executed one after the other
)

# Begin the task execution
tech_crew.kickoff()
