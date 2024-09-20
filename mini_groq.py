import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import groq

# Créer une instance de FastAPI
app = FastAPI()

# Configurer le client Groq
client = groq.Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
    timeout=20.0,
    max_retries=1,
)

# Définir un modèle de données pour les requêtes POST
class Prompt(BaseModel):
    prompt: str

# Définir un point de terminaison GET pour vérifier l'état
@app.get("/status")
async def get_status():
    return {"message": "OK"}

# Définir un point de terminaison POST pour obtenir des réponses du chatbot
@app.post("/chat")
async def post_chat(prompt: Prompt):
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt.prompt},
            ],
            model="mixtral-8x7b-32768",
        )
        return {"response": chat_completion.choices[0].message.content}

    except groq.APIConnectionError as e:
        raise HTTPException(status_code=500, detail="API Connection Error")

    except groq.RateLimitError as e:
        raise HTTPException(status_code=429, detail="Rate Limit Exceeded")

    except groq.APIStatusError as e:
        raise HTTPException(status_code=e.status_code, detail="API Status Error")

# Exécuter l'application avec Uvicorn si ce fichier est exécuté directement
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
