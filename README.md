# GEN AI FAQ Chatbot

  
Few years back, to implement a chatbot you have to define intents, group relevant utterences together and define named entities.


With the emerge of Large Language Models, would it be possible to implement a Chatbot without defining intents?

This repository use the class insurance QA dataset, Azure OpenAI, Azure AI Search to implement an Insurance FAQ Chatbot without defining intents

## Architecture

![Architecture for the project](./images/InsuranceQA_Architect.png)

## Prerequisite

- Azure AI Search
- Azure OpenAI or OpenAI or Ollama

## Features

- Just ask a question about insurance policies, claims, and more!

![Screenshot of Chat UI](./images/chat_ui_screenshot.png)

- Promt Template used:

```
template="""
        You are a helpful contact centre agent of an big insurance company. You will answer user enquiry based on provided dataset snippets.
        The dataset is about insurance questions and answers. The dataset contains 3 colummns: id, question, answer.
        You must answer the user query using the exact answer from the dataset snippets and do not make up any answers.
        User query: {user_query}
        Dataset snippets: {docs}
        """
```
## Setup

- Clone this repository.
- Create a [virtual environment.](https://docs.python.org/3/library/venv.html)
- Install the required Python packages:

``` python
pip install -r requirements.txt
```

- Set up your Azure AI Search service and get your endpoint URL and admin key.
- Set up your Azure OpenAI service and get your endpoint URL and admin key.
- Deploy text-embedding-ada-002 and gpt-4.1 in Azure OpenAI
- If you use ollama, download gemma3:12b
- Create a .env file in the root directory of the project and add your Azure Search endpoint URL, admin key, Azure OpenAI endpoint URL and API key (look at the `.env.example):

``` bash
AZURE_SEARCH_ENDPOINT="<YOUR_AZURE_SEARCH_ENDPOINT_URL>"
AZURE_SEARCH_ADMIN_KEY="<YOUR_AZURE_SEARCH_ADMIN_KEY>"
AZURE_OPENAI_API_KEY="<YOUR_AZURE_OPENAI_API_KEY>"
AZURE_OPENAI_ENDPOINT="<YOUR_AZURE_OPENAI_ENDPOINT_URL>"
OPENAI_API_KEY="<YOUR_OPENAI_API_KEY>"
LLM_PROVIDER="azure_openai"
```

## Usage

1. Run the Streamlit application:
``` python
streamlit run streamlit.py
```
2. Open the application in your web browser.
3. Ask a question about insurance policies, claims, etc.
4. Click the "Submit" button to generate an answer.

## Author

- GitHub: [@samueltin](https://github.com/samueltin)
