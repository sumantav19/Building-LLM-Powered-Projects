from openai import OpenAI
# import math
# import numpy 

client = OpenAI(
   base_url="http://localhost:1234/v1",
   api_key="lm-studio"
)

def read_file( file_path ):
    with open(file_path,'r',encoding='utf-8') as file:
        text =  file.read()
    return text

# def chunk_text(text,chunk_size):
#     chunk = [text[i:i+chunk_size] for i in range(0,len(text),chunk_size)]
#     return chunk

# def dot_product(vec1,vec2):
#     return sum(a * b for a, b in zip(vec1,vec2))

# def magnitude(vec):
#     return math.sqrt(sum(v**2 for v in vec))

# def cosine_similarity(vec1,vec2):
#     dot_prod = dot_product(vec1,vec2)
#     mag_vec1 = magnitude(vec1)
#     mag_vec2 = magnitude(vec2)

#     if mag_vec1 == 0 or mag_vec2 == 0:
#         return 0
    
#     return dot_prod / (mag_vec1 * mag_vec2)

client = OpenAI(
   base_url="http://localhost:1234/v1",
   api_key="lm-studio"
)

def get_embedding(text,model):
    return client.embeddings.create(
        input = text,
        model = model
    ).data[0].embedding
    

text_file = read_file("/Users/sumant/workspace/learning/llm_projects/building_llm_powered_projects/project2/context/harry_potter_sorcerrer_stone.txt")

query = "What is greatest fear of Dursleys?"
# The role in prompt for system modifies the answer
system_message = f"You are a Reader. A user will ask  you with relevant information.\
    Your task is to answer the question and using the provided information."
question = "Question - {query}" 

response = client.chat.completions.create(
    model = "gpt-3.5-turbo",
    messages = [
        {
            "role":"system","content" : system_message
        },
        { "role":"user","content":query },
        { "role" : "user" ,"content":"Information - {text_file}"} # the information will be provided is mentioned in prompt so I prefixed the text file with information.
    ]
)
response_dict = response.model_dump()
print(response_dict["choices"][0]["message"]["content"])