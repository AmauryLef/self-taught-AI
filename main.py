import os
from dotenv import load_dotenv
load_dotenv()

from agents.researcher import researcher
from agents.writer import writer
from agents.coder import coder
from agents.local_agent import local_agent

AGENTS = {
    "recherche": researcher,
    "rédaction": writer,
    "code": coder,
    "local": local_agent,
}

print("Choisis un agent : recherche / rédaction / code / local")
print("Tape 'switch' pour changer d'agent, 'quit' pour quitter.\n")

agent_name = input("Agent : ").strip().lower()
agent = AGENTS.get(agent_name, researcher)
print(f"Agent '{agent_name}' prêt !\n")

while True:
    question = input("Toi : ").strip()
    if question.lower() == "quit":
        break
    if question.lower() == "switch":
        agent_name = input("Nouvel agent : ").strip().lower()
        agent = AGENTS.get(agent_name, researcher)
        print(f"Switched vers '{agent_name}'\n")
        continue

    result = agent.invoke({
        "messages": [{"role": "user", "content": question}]
    })
    print(f"\n{agent_name.capitalize()} : {result['messages'][-1].content}\n")