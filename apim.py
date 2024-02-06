from langchain.schema import HumanMessage
from langchain_openai import AzureChatOpenAI
from langchain.globals import set_verbose, set_debug
from dotenv import load_dotenv

load_dotenv()

set_verbose(False)
set_debug(True)

model = AzureChatOpenAI(
    deployment_name="gpt-35-turbo-0613",
    model_name="gpt-35-turbo",
    openai_api_version="2023-05-15",
    streaming=False,
)

message = HumanMessage(
    content="Translate this sentence from English to French: 'Hello, world!.'"
)

model.invoke(input=[message])
