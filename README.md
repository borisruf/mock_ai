# MockAI
A Python library which simulates the use of cloud-based API models for educational purposes.

## Installation

To install the package, you can use `pip`, the Python package manager. Open a command line or terminal and run the following command:

```bash
pip install git+https://github.com/borisruf/mockai.git
```

## Usage

Once the package is installed, you can include and use it in your Python code as follows:

```python
import os
from mockai import MockAzureOpenAI

AZURE_ENDPOINT = os.getenv("AZURE_ENDPOINT")
OPENAI_MODEL = os.getenv("OPENAI_MODEL")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = MockAzureOpenAI(azure_endpoint=AZURE_ENDPOINT, api_key=OPENAI_API_KEY)

response = client.chat.completions.create(model=OPENAI_MODEL, messages=[{"role": "system", "content": "What is the origin of the Olympic Games?"}])

print(response)
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

Use [create_cache.py](https://github.com/borisruf/mockai/blob/main/mockai/create_cache.py) to modify or enhance the list of cached requests.
