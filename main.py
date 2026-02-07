from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain.tools import tool
import datetime

# load stuff
load_dotenv()

# variables
video_api = os.getenv("MEMORIESAI_API")
idea = '''Winter Soldier vs. Cap fight scene. Caption: "When your bestie signs up for Campfire without telling you."'''

@tool
def get_time():
    """Get current time in this format: hh:mm:ss"""
    time = datetime.datetime.now()
    return f"{time.hour}:{time.minute}:{time.second}"

llm = ChatOpenAI(
    model="gpt-5-mini",
    api_key=os.getenv("HACKCLUB_AI_API"),
    base_url="https://ai.hackclub.com/proxy/v1"
)

tools = [get_time]

agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt="You are a coder"
)

reponse = agent.invoke(
    {"messages": [{"role": "user", "content": "What is time right now"}]}
)

print(reponse)
