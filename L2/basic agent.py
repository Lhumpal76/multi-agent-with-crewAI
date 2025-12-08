from crewai import Agent, LLM

# # Example using Gemini's OpenAI-compatible API
# llm = LLM(
#     model="openai/gemini-2.0-flash",
#     base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
#     api_key="AIzaSyAarvzNAjFo8w0e3B75cdKxOeNAxz-tR8U",  # Should start with AIza...
# )

# Use Ollama locally
llm = LLM(
    model="ollama/mistral",        # or whatever model you pulled
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