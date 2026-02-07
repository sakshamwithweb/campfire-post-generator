from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
import os


def init_agent(system_prompt, tools):
    llm = ChatOpenAI(
        model="gpt-5-mini",
        api_key=os.getenv("HACKCLUB_AI_API"),
        base_url="https://ai.hackclub.com/proxy/v1"
    )

    agent = create_agent(
        model=llm,
        tools=tools,
        system_prompt=system_prompt
    )

    return agent
