import os
from openai import AzureOpenAI
import json
import random
import string
import pickle

AZURE_ENDPOINT = os.getenv("OPENAI_API_BASE")
OPENAI_MODEL_NAME = os.getenv("OPENAI_MODEL_NAME")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


# List of prompts within a limited scope for simulation purposes, here questions about the Olympic Games
prompts = [
    "What is the origin of the Olympic Games?",
    "How often are the Olympic Games held?",
    "Which city has hosted the Olympics the most times?",
    "What are the main symbols of the Olympic Games?",
    "What is the Olympic motto?",
    "What is the Olympic flame?",
    "What are the core sports in the modern Olympic Games?",
    "What is the significance of the Olympic rings?",
    "What is the Olympic Oath?",
    "What are the Paralympic Games?"
]

client = AzureOpenAI(azure_endpoint=AZURE_ENDPOINT, api_key=OPENAI_API_KEY)

# Generate random id for chat completion response
random_chat_completion_id = 'chatcmpl-'.join(random.choice(string.ascii_letters + string.digits) for _ in range(30))

if os.path.exists('cache.pickle'):
    with open('cache.pickle', 'rb') as f:
        queries = pickle.load(f)
else:
    queries = {}

queries[OPENAI_MODEL_NAME] = {}


for prompt in prompts:

    answers = []

    for i in range(3):
        response = client.chat.completions.create(model=OPENAI_MODEL_NAME, messages=[{"role": "system", "content": prompt}])
        response.id = random_chat_completion_id
        answers.append(response)

    queries[OPENAI_MODEL_NAME][prompt] = answers

answers = []

# Generate a few default responses to use when there is no match
for i in range(3):
    response = client.chat.completions.create(model=OPENAI_MODEL_NAME, messages=[{"role": "system", "content": "Write a short answer which states that you do not know the answer."}])
    response.id = random_chat_completion_id
    answers.append(response)

queries[OPENAI_MODEL_NAME]["default"] = answers

# Cache all responses in a pickle
with open('cache.pickle', 'wb') as file:
    pickle.dump(queries, file)