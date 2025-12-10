from crewai import Agent, LLM

# Use Ollama locally
llm = LLM(
    model="ollama/",        # or whatever model you pulled
    base_url="http://localhost:11434"
    # no api_key needed
)

# Create an agent
agent = Agent(
    role="Content Planner",
    goal="Plan engaging and factually accurate content on",
    backstory="You're working on planning a blog article "
              "about the topic: ."
              "You collect information that helps the "
              "audience learn something "
              "and make informed decisions. "
              "Your work is the basis for "
              "the Content Writer to write an article on this topic.",
    allow_delegation=False,
    llm=llm,
	verbose=True
)


# Example usage
# Call the agent directly
response = agent.kickoff("Hello! Can you summarize what you do?")
print(response)