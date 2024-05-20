from llama_index.llms.azure_openai import AzureOpenAI

api_key = "4f1a2cb0283f4fbabe4a76d498b3073c"
azure_endpoint = "https://openaiazure123.openai.azure.com/"
api_version = "2024-02-15-preview"

llm = AzureOpenAI(
    model="gpt-35-turbo",
    deployment_name="gpt-35-turbo",
    api_key=api_key,
    azure_endpoint=azure_endpoint,
    api_version=api_version,
)

response = llm.complete("The sky is a beautiful blue and")
print(response)

from llama_index.core.llms import ChatMessage

messages = [
    ChatMessage(
        role="system", content="You are a pirate with colorful personality."
    ),
    ChatMessage(role="user", content="Hello"),
]

response = llm.chat(messages)
print(response)
