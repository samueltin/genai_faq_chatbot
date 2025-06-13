# Import required modules
import os
from langchain_openai import OpenAI, AzureOpenAI
from langchain.prompts import PromptTemplate
from langchain_community.vectorstores.azuresearch import AzureSearch
from langchain_openai import OpenAIEmbeddings, AzureOpenAIEmbeddings, AzureChatOpenAI, ChatOpenAI
from dotenv import load_dotenv
from langchain.schema import HumanMessage
from langchain_ollama import ChatOllama

# Load environment variables from .env file
load_dotenv()

# Use an Azure OpenAI account with a deployment of an embedding model
azure_endpoint: str = os.getenv("AZURE_OPENAI_ENDPOINT")
azure_openai_api_key: str = os.getenv("AZURE_OPENAI_API_KEY")
azure_openai_api_version: str = "2023-05-15"
azure_deployment: str = "text-embedding-ada-002"

vector_store_address: str = os.getenv("AZURE_SEARCH_ENDPOINT")
vector_store_password: str = os.getenv("AZURE_SEARCH_ADMIN_KEY")
index_name: str = "insurance-faqs"
llm_provider: str = os.getenv("LLM_PROVIDER", "azure_openai")


# Use AzureOpenAIEmbeddings with an Azure account
embeddings: AzureOpenAIEmbeddings = AzureOpenAIEmbeddings(
    azure_deployment=azure_deployment,
    openai_api_version=azure_openai_api_version,
    azure_endpoint=azure_endpoint,
    api_key=azure_openai_api_key,
)

# Initialize AzureSearch with the endpoint, key, index name, and embedding function
index_name: str = "insurance-faqs"
vector_store: AzureSearch = AzureSearch(
    azure_search_endpoint=vector_store_address,
    azure_search_key=vector_store_password,
    index_name=index_name,
    embedding_function=embeddings.embed_query,
)

def create_chat_llm():
    if llm_provider == "azure_openai":
        return AzureChatOpenAI(
            openai_api_key=azure_openai_api_key,
            azure_endpoint=azure_endpoint,
            openai_api_version='2024-12-01-preview',
            deployment_name='gpt-4.1',
            openai_api_type="azure"
        )
    elif llm_provider == "openai":
        return ChatOpenAI(
            model="gpt-4o",
            temperature=0
        )
    elif llm_provider == "ollama":
        return ChatOllama(model="deepseek-r1")

def query_llm(user_query, k=1):


    # Perform a similarity search on the vector store
    documents = vector_store.similarity_search(
    query=user_query,
    k=k,
    search_type="similarity",
    )


    # Join the page content of the returned documents
    docs = " ".join([d.page_content for d in documents])

    chat = create_chat_llm()

    prompt = PromptTemplate(
        input_variables=["user_query", "docs"],
        template="""
        You are a helpful contact centre agent of an big insurance company. You will answer user enquiry based on provided dataset snippets.
        The dataset is about insurance questions and answers. The dataset contains 3 colummns: id, question, answer.
        You must answer the user query using the exact answer from the dataset snippets and do not make up any answers.
        User query: {user_query}
        Dataset snippets: {docs}
        """,
    )
    
    chain = prompt | chat
    
    response = chain.invoke({"user_query":user_query, "docs":docs})
    
    return response

if __name__ == "__main__":
    # user_query = "Is Garage Door Covered By Homeowners Insurance?"
    user_query = "Does homeowners insurance cover garage doors?"
    response = query_llm(user_query=user_query, k=10)
    print(response.content)