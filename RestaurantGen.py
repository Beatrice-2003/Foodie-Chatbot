import getpass
from dotenv import load_dotenv
import os
from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
#from langchain_core.tools import tool
#from langchain.agents import AgentExecutor, create_tool_calling_agent
#from langchain_community.agent_toolkits.load_tools import load_tools

load_dotenv()

if os.getenv("AZURE_OPENAI_API_KEY") is None or os.getenv("AZURE_OPENAI_API_KEY") == "":
        print("AZURE_OPENAI_API_KEY is not set")
        exit(1)
else: 
        print("AZURE_OPENAI_API_KEY is set")   

if os.getenv("AZURE_OPENAI_ENDPOINT") is None or os.getenv("AZURE_OPENAI_ENDPOINT") == "":
        print("AZURE_OPENAI_ENDPOINT is not set")
        exit(1)
else: 
        print("AZURE_OPENAI_ENDPOINT is set")


def restaurant_recommendations(destination_country: str, food: str, output_langauge: str, phrase:str) -> str:
    """Generates the best restaurant recommendations for a specific food delicacy in a country of choice and communicates in the desired language"""
    llm = AzureChatOpenAI(
        azure_deployment="gpt4o",
        api_version="2024-08-01-preview",
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2
    )

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are a helpful cuisine assistant that translates a phrase to any {language}, and recommends the best restaurants to a traveler that is in a specific {country}, and would like to try out a specific {food}, and adds some emojjis to add foody feel to the response"
            ),
            ("human", "{country}, {food}, {phrase}"),
        ]
    )

    chain = prompt | llm

    ai_output = chain.invoke(
        {
            "country": destination_country,
            "food": food,
            "language": output_langauge,
            "phrase": phrase
        }

    )

    return ai_output.content