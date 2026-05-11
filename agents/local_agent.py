from deepagents import create_deep_agent
from tools.local import find_file, read_file, list_directory, open_file

local_agent = create_deep_agent(
    model="ollama:llama3.2",
    tools=[find_file, read_file, list_directory, open_file],
    system_prompt="""Tu es un assistant qui gère les fichiers locaux.
    Tu peux chercher, lire, lister et ouvrir des fichiers sur le PC.
    Quand on te demande de trouver un fichier, utilise find_file.
    Quand on te demande de lire un fichier, utilise read_file.
    Quand on te demande d'ouvrir un fichier, utilise open_file.""",
)