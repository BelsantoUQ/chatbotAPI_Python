import openai
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/chatbotUQ")
def chatear(question: str):
    openai.api_key = "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"
    conversation = ""

    conversation += "\nHumano: "+ question + "\nAI:"
    
    response = openai.Completion.create(
        engine = "davinci",
        prompt=conversation,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=["\n", " Humano:", " AI:"]
    )

    answer = response.choices[0].text.strip()
    conversation +=answer
    print("AI: "+answer+"\n")
    return {answer}

