import asyncio
from browser_use import Agent
from langchain_openai import ChatOpenAI

async def main():
    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0
    )

    agent = Agent(
        task="""
        Go to https://en.wikipedia.org/wiki/Artificial_intelligence
        Summarize the content.
        """,
        llm=llm
    )

    await agent.run()

asyncio.run(main())