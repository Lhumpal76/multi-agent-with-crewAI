# load .env
from dotenv import load_dotenv
load_dotenv()

import requests
import urllib3

# ------------------------
# CrewAI setup
# ------------------------
from crewai import Agent, LLM, Task, Crew
from crewai_tools import ScrapeWebsiteTool

llm = LLM(
    model="ollama/Mistral",
    base_url="http://localhost:11434"
)

support_agent = Agent(
    role="Senior Support Representative",
    goal="Be the most friendly and helpful support representative",
    backstory=(
        "You work at crewAI and are now providing support "
        "to {customer}. Make sure to give complete, accurate, and friendly answers."
    ),
    llm=llm,
    allow_delegation=False,
    verbose=True
)

support_quality_assurance_agent = Agent(
    role="Support QA Specialist",
    goal="Ensure the support representative delivers the highest quality answers",
    backstory=(
        "You work at crewAI ensuring that support is complete and accurate."
    ),
    llm=llm,
    verbose=True
)

docs_scrape_tool = ScrapeWebsiteTool(
    website_url="https://docs.crewai.com/how-to/Creating-a-Crew-and-kick-it-off/"
)

inquiry_resolution = Task(
    description=(
        "{customer} has an inquiry:\n"
        "{inquiry}\n"
        "Respond fully and accurately using all resources."
    ),
    expected_output=(
        "Provide a complete, helpful answer, with references to all sources used."
    ),
    tools=[docs_scrape_tool],
    agent=support_agent,
)

quality_assurance_review = Task(
    description=(
        "Review the response for {customer}, ensuring completeness, accuracy, and helpful tone."
    ),
    expected_output=(
        "Final detailed response, ready to send, fully addressing the inquiry."
    ),
    agent=support_quality_assurance_agent,
)

crew = Crew(
    agents=[support_agent, support_quality_assurance_agent],
    tasks=[inquiry_resolution, quality_assurance_review],
    verbose=True,
    memory=False, # Short term memory uses RAG with openAI embedding
)

# ------------------------
# Run CrewAI
# ------------------------
inputs = {
    "customer": "DeepLearningAI",
    "inquiry": "How can I add memory to my crew? Provide guidance."
}

# just run kickoff normally
result = crew.kickoff(inputs=inputs)
output_text = result.raw

# Display output
from IPython.display import Markdown
Markdown(output_text)
