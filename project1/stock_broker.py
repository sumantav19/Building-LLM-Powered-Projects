#improve the prompt
from openai import OpenAI

client = OpenAI(
   base_url="http://localhost:1234/v1",
   api_key="lm-studio"
)


system_message = """

You are a Stock assistant that suggest about the performance of a company.

Text will contain the name of a stock.

Give the current and expected operating profit  . Explain the operating profit.

If the text is random stock suggest the user with name of stock they may be looking for.

Otherwise, inform the user that the text does not contain a valid name.

Text:

"""

instructions = """

Tell me about Hindustan Unilever?

"""

response = client.chat.completions.create(
    model = "gpt-3.5-turbo",
    messages = [
        {
            "role" : "system" , "content" : system_message
        },
        {
            "role" : "user" ,  "content" : instructions
        }
    ]
)
response_dict = response.model_dump()
print(response_dict["choices"][0]["message"]["content"])