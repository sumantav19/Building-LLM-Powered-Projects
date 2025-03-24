from openai import OpenAI

client = OpenAI(
   base_url="http://localhost:1234/v1",
   api_key="lm-studio"
)

system_message = """

You are a motor bike mechanic that helps inexperienced humans by generating instructions for motor bike maintenance.

You will be provided with a question. The question will be for a motor bike part. Generate instructions for maintenance in bullet points.

Identify the main steps, highlight and provide elaborate instruction for the same.

Identify and give warnings for hazardous steps and provide steps for the same.

If the question is not for a motor bike part, inform the user that the question is not valid.

Question:

"""

question = """

How can I maintain the chain of a Royal Enfield Thunderbird 350? 

"""

response = client.chat.completions.create(
    model = "gpt-3.5-turbo",
    messages = [
        {
            "role" : "system" , "content" : system_message
        },
        {
            "role" : "user" ,  "content" : question
        }
    ]
)
response_dict = response.model_dump()
print(response_dict["choices"][0]["message"]["content"])