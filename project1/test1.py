# import os
from openai import OpenAI

client = OpenAI(
   base_url="http://localhost:1234/v1",
   api_key="lm-studio"
)

# openai.api_key = os.environ.get("OPEN_AI_KEY")


system_message = """

You are an AI assistant that helps humans by generating tutorials given a text.

You will be provided with a text. If the text contains any kind of instructions on how to proceed with something, generate a tutorial in a bullet list.

Otherwise, inform the user that the text does not contain any instructions.

Text:

"""

instructions = """

To prepare the known sauce from Genova, Italy, you can start by toasting the pine nuts to then coarsely

chop them in a kitchen mortar together with basil and garlic. Then, add half of the oil in the kitchen mortar and season with salt and pepper.

Finally, transfer the pesto to a bowl and stir in the grated Parmesan cheese.

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