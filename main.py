from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

app = FastAPI(title = "Junior ML Engineer Test - Translation Service")

# In-memory database for storing translation pairs. This is simply a list that holds dictionaries. 
translation_db = []

def compute_embedding(sentence: str) -> np.ndarray:
    """
    Compute a simple fixed-length embedding using frequency of letters a to z.
    Convert the sentence to lowercase and count the frequency of each letter.
    Normalize the resulting vector.
    """
    sentence = sentence.lower()
    vec = np.zeros(26)
    for char in sentence:
        if char.isalpha():
            idx = ord(char) - ord('a')
            if 0 <= idx < 26:
                vec[idx] += 1
    norm = np.linalg.norm(vec)
    return vec / norm if norm > 0 else vec



# Pydantic model for incoming translation pair requests
class TranslationPair(BaseModel):
    source_lang: str = Field(..., alias="source_language")
    target_lang: str = Field(..., alias="target_language")
    sentence: str
    translation: str

    class Config:
        allow_population_by_field_name = True  # This allows you to use the field names in your code.


# Pydantic model for prompt requests (if needed to use as JSON body)
class PromptRequest(BaseModel):
    source_lang: str
    target_lang: str
    query_sentence: str
    
# Endpoint to add a new translation pair
@app.post("/pairs", summary = "add a translation pair")
def add_translation_pair(pair: TranslationPair):
    # compute a single embedding for the source sentence
    embedding = compute_embedding(pair.sentence)
    # Store the pair along with its embedding
    translation_db.append({
        "source_lang": pair.source_lang,
        "target_lang": pair.target_lang,
        "sentence": pair.sentence,
        "translation": pair.translation,
        "embedding": embedding
    })
    return {"status": "ok"}


# Endpoint to generate a translation prompt based on a query sentence
@app.get("/prompt", summary="Retrieve a translation prompt")
def get_translation_prompt(source_language: str, target_language: str, query_sentence: str):
    source_lang = source_language
    target_lang = target_language
    
    if not translation_db:
        raise HTTPException(status_code=404, detail="No translation pairs available.")
    
    query_embedding = compute_embedding(query_sentence)
    similarities = []
    # Collect similarity scores for matching pairs.
    for pair in translation_db:
        if pair["source_lang"] == source_lang and pair["target_lang"] == target_lang:
            sim = cosine_similarity(query_embedding.reshape(1, -1),
                                    pair["embedding"].reshape(1, -1))[0][0]
            similarities.append((sim, pair))
    
    # Build the prompt irrespective of whether any matching pairs are found.
    prompt = f"Please translate the following sentence from {source_lang} to {target_lang}:\n'{query_sentence}'\n\n"
    
    if similarities:
        # Sort and take the top 4 sample pairs if available.
        similarities.sort(key=lambda x: x[0], reverse=True)
        top_pairs = [pair for _, pair in similarities[:4]]
        prompt += "Here are some sample translations for reference:\n"
        for idx, pair in enumerate(top_pairs, start=1):
            prompt += f"{idx}. {pair['sentence']}  -->  {pair['translation']}\n"
    else:
        # Instead of returning a 404, provide a fallback message.
        prompt += "No sample translations available."
    
    return {"prompt": prompt}


# This block is useful if you want to run the server directly with Python.
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")