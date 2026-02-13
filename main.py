from dotenv import load_dotenv
from agent import init_agent
from tools import tools
import os

# load stuff
load_dotenv()

# variables
# video_api = os.getenv("MEMORIESAI_API")
# idea = '''Winter Soldier vs. Cap fight scene. Caption: "When your bestie signs up for Campfire without telling you."'''

agent = init_agent("You only do what is said", tools)

response = agent.invoke(
    {"messages": [{"role": "user", "content": "search doreamon video in which nobita asks for a robot but doreamon says he already have one but nobita asks several question like do you have weapons like him then doreamon open his pocket and get nuclear bomb"}]}
)

messages = response["messages"]
print(messages[len(messages)-1].content)
