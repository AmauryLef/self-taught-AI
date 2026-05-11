from deepagents import create_deep_agent
from tools.search import internet_search

writer = create_deep_agent(
    model="ollama:llama3.2",
    tools=[internet_search],
    system_prompt="""Tu es un expert en rédaction.
    Tu écris des textes clairs, structurés et engageants.
    Tu t'adaptes au ton demandé (formel, casual, technique...).""",
)