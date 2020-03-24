# web_app/services/basilica_services.py

import os
from dotenv import load_dotenv
import basilica

load_dotenv()

API_KEY = os.getenv('BASILICA_API_KEY')

connection = basilica.Connection(API_KEY)

sentence = 'Hey you!'
sent_embeddings = connection.embed_sentence(sentence)
print('----------------')
print(sent_embeddings)

print('----------------')
print('----------------')

sentences = ["Hello world!", "How are you?"]
embeddings = connection.embed_sentences(sentences)
print('----------------')
print('EMBEDDINGS:')
print(type(embeddings))
print(list(embeddings)) # [[0.8556405305862427, ...], ...]