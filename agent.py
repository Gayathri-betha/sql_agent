import openai
import streamlit as st
import os
from langchain.utilities import SQLDatabase
from langchain.llms import OpenAI
from langchain.agents.agent_types import AgentType
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.utilities import SQLDatabase
from langchain_openai import OpenAI
from langchain.agents import create_sql_agent
from dotenv import load_dotenv

# Streamlit app title
st.title("SQL Agent")

# Function to load the OpenAI API key securely (replace with your implementation)
def load_openai_key():
  """Loads the OpenAI API key from a secure location (e.g., environment variables)."""
  openai.api_key = os.getenv("OPENAI_API_KEY")
  if not openai.api_key:
    raise EnvironmentError("Missing environment variable: OPENAI_API_KEY")

# Load the OpenAI API key (replace with secure loading mechanism)
load_openai_key()

# Define the database URI (replace with your actual connection string)
db_uri = 'sqlite:///sql_lite_database.db'

# Define the SQL database connection
db = SQLDatabase.from_uri(db_uri)

# Choose the LLM model (default OpenAI model in this case)
llm = OpenAI(
    temperature=0,
    verbose=True,
)

# Setup agent toolkit with database and LLM
toolkit = SQLDatabaseToolkit(db=db, llm=llm)

# Create the SQL agent
agent_executor = create_sql_agent(
    llm=llm,
    toolkit=toolkit,
    verbose=True,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
)

# Session state for chat messages
if "messages" not in st.session_state:
  st.session_state.messages = []

# Display past chat messages
for message in st.session_state.messages:
  with st.chat_message(message["role"]):
    st.markdown(message["content"])

# User prompt input
if prompt := st.chat_input("What is up?"):
  # Add user message to session state
  st.session_state.messages.append({"role": "user", "content": prompt})

  with st.chat_message("user"):
    st.markdown(prompt)

  try:
    # Get agent response and add it to session state
    response = str(agent_executor.invoke(prompt)["output"])
    st.session_state.messages.append({"role": "assistant", "content": response})

    with st.chat_message("assistant"):
      st.write(response)
  except Exception as e:
    st.error(f"An error occurred: {e}")

