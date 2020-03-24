# web_app/services/basilica_services.py

import os
from dotenv import load_dotenv
import basilica

load_dotenv()

API_KEY = os.getenv('BASISILICA_API_KEY')

with basilica.Connection(API_KEY) as c:
    embeddings = c.embed_sentences(["Hello world!", "How are you?"])
    print('----------------')
    print(list(embeddings)) # [[0.8556405305862427, ...], ...]