# SQL Agent

## Overview
SQL Agent is a Streamlit-based chatbot that interacts with an SQL database using OpenAI's LLM and LangChain. It enables users to query databases in natural language and receive structured responses.

## Features
- Interactive chatbot interface
- Natural language queries to SQL database
- Uses OpenAI's LLM via LangChain
- Supports SQLite databases

## Installation
### Prerequisites
- Python 3.8+
- SQLite
- OpenAI API key

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/sql-agent.git
   cd sql-agent
   ```
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a `.env` file and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your-api-key-here
   ```
5. Run the application:
   ```bash
   streamlit run app.py
   ```

## Usage
1. Enter your OpenAI API key in the Streamlit interface.
2. Input your SQL queries in natural language.
3. View structured responses from the database.


## Acknowledgments
Built with OpenAI, LangChain, and Streamlit.

