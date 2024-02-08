from langchain.schema import HumanMessage
from langchain_openai import AzureChatOpenAI
from langchain_community.callbacks import get_openai_callback
from langchain.globals import set_debug
from dotenv import load_dotenv

load_dotenv()
set_debug(False)

model = AzureChatOpenAI(
    deployment_name="gpt-35-turbo-0613",
    model_name="gpt-35-turbo",
    openai_api_version="2023-05-15",
    streaming=False,
)

input_question = "What is the wing speed velocity of an unladen swallow?"
print(f"\nInput: {input_question}")

message = HumanMessage(content=input_question)

with get_openai_callback() as callback:
    res = model.invoke(input=[message])
    print(f"\nResponse: {res.content}\n")

    print(res)

    if model.streaming == False:
        print(f"Callback:\n{callback}\n")
