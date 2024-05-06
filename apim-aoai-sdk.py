from openai import AzureOpenAI
from dotenv import load_dotenv

# API Key from AZURE_OPENAI_API_KEY environment variable
# Endpoint from AZURE_OPENAI_ENDPOINT environment variable
load_dotenv()
client = AzureOpenAI(
    api_version="2023-05-15",
)

completion = client.chat.completions.create(
    model="gpt-35-turbo-0613", # deployment name
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the wing speed velocity of an unladen swallow?"},
    ],
)

print(completion.to_json())
