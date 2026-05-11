from deepagents import create_deep_agent
from tools.search import internet_search

coder = create_deep_agent(
    model="ollama:llama3.2",
    tools=[internet_search],
    system_prompt="""Tu es un expert en programmation.
    Tu écris du code propre et commenté.
    Tu expliques toujours ce que tu fais et pourquoi.""",
)