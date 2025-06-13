import os

from langchain_community.vectorstores.azuresearch import AzureSearch
from langchain_openai import AzureOpenAIEmbeddings, OpenAIEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter


from dotenv import load_dotenv

load_dotenv()

# Use an Azure OpenAI account with a deployment of an embedding model
azure_endpoint: str = os.getenv("AZURE_OPENAI_ENDPOINT")
azure_openai_api_key: str = os.getenv("AZURE_OPENAI_API_KEY")
azure_openai_api_version: str = "2023-05-15"
azure_deployment: str = "text-embedding-ada-002"

# Configure vector store settings
vector_store_address: str = os.getenv("AZURE_SEARCH_ENDPOINT")
vector_store_password: str = os.getenv("AZURE_SEARCH_ADMIN_KEY")
index_name: str = "insurance-faqs"

# Use AzureOpenAIEmbeddings with an Azure account
embeddings: AzureOpenAIEmbeddings = AzureOpenAIEmbeddings(
    azure_deployment=azure_deployment,
    openai_api_version=azure_openai_api_version,
    azure_endpoint=azure_endpoint,
    api_key=azure_openai_api_key,
)



# Initialize the Azure Search vector store
vector_store: AzureSearch = AzureSearch(
    azure_search_endpoint=vector_store_address,
    azure_search_key=vector_store_password,
    index_name=index_name,
    embedding_function=embeddings.embed_query
)


def create_vector_store():
    """
    Create the vector store by loading documents and adding them to the Azure Search index.
    """
    # Load and chunk the documents
    loader = TextLoader("./data/question_answer.csv", encoding="utf-8")
    documents = loader.load()
    text_splitter = CharacterTextSplitter(
    chunk_size=800,     # maximum characters per chunk
    chunk_overlap=80,   # overlap between chunks
    separator="\n"
    )
    docs = text_splitter.split_documents(documents)
    print(f"Number of documents loaded: {len(docs)}")

    # Add documents to the vector store
    vector_store.add_documents(docs)

def similarity_search(query, k=4):
    """
    Perform a similarity search on the vector store.
    
    Args:
        query (str): The query string to search for.
        k (int): The number of results to return.
    
    Returns:
        list: A list of documents that match the query.
    """
    return vector_store.similarity_search(query=query, k=k, search_type="similarity")

if __name__ == "__main__":
    # create_vector_store()  # Uncomment to create the vector store if not already created

    # Example usage
    query = "Does homeowners insurance cover garage doors?"
    results = similarity_search(query, k=4)
    
    for doc in results:
        print(f"Document: {doc.page_content}\n")
        print(f"Metadata: {doc.metadata}\n")