import random
import time
import difflib
import pickle
import warnings
import os

class StubAzureOpenAI:
    class chat:
        class completions:
            def create(model, messages, temperature=1, max_tokens=16, top_p=1, frequency_penalty=0, presence_penalty=0, stop=None):

                    path = os.path.join(os.path.dirname(__file__), 'cache.pickle')

                    with open(path, 'rb') as f:
                        cache = pickle.load(f)

                    if model in cache.keys():
   
                        # Fuzzy match query to cached queries
                        match = difflib.get_close_matches(messages[0]['content'], cache[model].keys(), n=1, cutoff=0.9)
                        key = match[0] if match else 'default' # Use default responses if no match
                        
                        responses = cache[model].get(key)
                
                        # Randomly delay response to simulate API request
                        time.sleep(random.uniform(1, 3))

                        # Randomly select one of the matching repsonses
                        return responses[random.randint(0, len(responses)-1)]

                    else:

                        warnings.warn(f"No cached data available for the AI model '{model}'. Currently supported models are: {str( ', '.join(list(cache.keys())))}")
                        return None


    def __init__(self, azure_endpoint, api_key, api_version=None):
        pass
