# Stub AI
A Python library which simulates the use of cloud-based AI models for educational purposes.

## Installation

To install the package, you can use `pip`, the Python package manager. Open a command line or terminal and run the following command:

```bash
pip install stub_ai
```

## Usage

Once the package is installed, you can include and use it in your Python code.

__Sample code:__

```python
from stub_ai import StubAzureOpenAI

AZURE_ENDPOINT = "[YOUR_AZURE_ENDPOINT]"
OPENAI_MODEL = "gpt-35-turbo"   # specify a supported model from the list
OPENAI_API_KEY = "[YOUR_OPENAI_API_KEY]"

client = StubAzureOpenAI(azure_endpoint=AZURE_ENDPOINT, api_key=OPENAI_API_KEY)

response = client.chat.completions.create(model=OPENAI_MODEL, messages=[{"role": "system", "content": "What is the origin of the Olympic Games?"}])

print(response.choices)
```

__Sample output:__
```bash
[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='The Olympic Games originated in ancient Greece around the 8th century BCE. They were held in Olympia, a small town in the western region of the Peloponnese. The Games were a religious festival dedicated to the Greek god Zeus and were held every four years. The first recorded Olympic Games took place in 776 BCE, and they continued for nearly 12 centuries until they were abolished in 393 CE by the Christian Byzantine Emperor Theodosius I.', role='assistant', function_call=None, tool_calls=None), content_filter_results={'hate': {'filtered': False, 'severity': 'safe'}, 'self_harm': {'filtered': False, 'severity': 'safe'}, 'sexual': {'filtered': False, 'severity': 'safe'}, 'violence': {'filtered': False, 'severity': 'safe'}})]
```

The `response` objects closely resemble the real API response without requiring actual API credentials. This makes it ideal for training scenarios, allowing users to experience the API's functionality without setup constraints.

Currently, the supported models include `gpt-35-turbo` and `gpt-4` and the following prompts, along with the following prompts:

- What is the origin of the Olympic Games?
- How often are the Olympic Games held?
- Which city has hosted the Olympics the most times?
- What are the main symbols of the Olympic Games?
- What is the Olympic motto?
- What is the Olympic flame?
- What are the core sports in the modern Olympic Games?
- What is the significance of the Olympic rings?
- What is the Olympic Oath?
- What are the Paralympic Games

Use [create_cache.py](https://github.com/borisruf/stub_ai/blob/main/stub_ai/create_cache.py) to modify or enhance the list of cached requests.
