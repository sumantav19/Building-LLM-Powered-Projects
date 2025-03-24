import math

def read_file( file_path ):
    with open(file_path,'r',encoding='utf-8') as file:
        text =  file.read()
    return text

def chunk_text(text,chunk_size):
    chunk = [text[i:i+chunk_size] for i in range(0,len(text),chunk_size)]
    return chunk

def get_model_name():
    return "bge-small-en-v1.5-gguf"

# def get_embedding_model():
#     embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")
#     return embed_model

# def get_embeddings(embed_model, text: str):
#     embeddings = embed_model.get_text_embedding(text)
#     return embeddings

def dot_product(vec1,vec2):
    return sum(a * b for a, b in zip(vec1,vec2))

def magnitude(vec):
    return math.sqrt(sum(v**2 for v in vec))

def cosine_similarity(vec1,vec2):
    dot_prod = dot_product(vec1,vec2)
    mag_vec1 = magnitude(vec1)
    mag_vec2 = magnitude(vec2)

    if mag_vec1 == 0 or mag_vec2 == 0:
        return 0
    
    return dot_prod / (mag_vec1 * mag_vec2)