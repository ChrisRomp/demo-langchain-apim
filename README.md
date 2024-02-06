# demo-langchain-apim
Demo calling Azure OpenAI with [LangChain](https://python.langchain.com/docs/get_started/introduction) via Azure API Management (APIM).

## Azure Environment

Your APIM will need to have Azure OpenAI REST API methods implemented (import OpenAPI spec from [docs](https://learn.microsoft.com/en-us/azure/ai-services/openai/reference)).

On your API, rename the subscription key header paramenter to `api-key`. Create an [APIM subscription](https://learn.microsoft.com/en-us/azure/api-management/api-management-subscriptions) with access to the APIs.

To run this sample, rename `.env.sample` to `.env` and populate the values for:

- `AZURE_OPENAI_API_KEY`: Your APIM subscription key
- `AZURE_OPENAI_ENDPOINT`: The URL to your APIM OpenAI APIs
