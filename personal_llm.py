import os
from langchain_openai import ChatOpenAI

# Read the API key from environment variables
openai_api_key = os.getenv("OPENAI_API_KEY")

# Pass the API key to the ChatOpenAI model
llm = ChatOpenAI(model="gpt-4o", temperature=0, openai_api_key=openai_api_key)