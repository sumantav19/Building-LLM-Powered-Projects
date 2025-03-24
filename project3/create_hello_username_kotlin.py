from openai import OpenAI

client = OpenAI(
   base_url="http://localhost:1234/v1",
   api_key="lm-studio"
)

## prompt
system_message = "You are an experienced software developer\
    Write user ask you to complete a task." \
    "Write the kotlin function" \
    "Follow the camel case naming convention for function name" \
    "Add arguments if required.\
        Add unit tests"

task = "write a function greet hello with user's name"

response = client.chat.completions.create(
    model = "deepseek-r1-distill-qwen-7b",
    messages = [
        {
            "role":"system","content" : system_message
        },
        { "role":"user","content":task }
        
    ]
)
response_dict = response.model_dump()
print(*response_dict)
print(response_dict["choices"][0]["message"]["content"])