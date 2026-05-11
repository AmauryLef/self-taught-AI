from deepagents import create_deep_agent
from tools.search import internet_search

researcher = create_deep_agent(
    model="ollama:llama3.2",
    tools=[internet_search],
    system_prompt="""Tu es un expert en recherche.
    Tu cherches des informations précises et récentes sur internet.
    Tu cites toujours tes sources.""",
)