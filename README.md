# sbai (Simple Broader AI)

A Python package to simplify interactions with OpenAI and Google Gemini APIs.

## Installation

```bash
pip install sbai
```

## Features

- Easy-to-use interfaces for ChatGPT and Gemini
- Configurable model parameters
- Optional conversation memory
- Support for system instructions

## Usage

### ChatGPT Integration

```python
from sbai import ChatGPT

# Initialize with OpenAI API key
client = ChatGPT(
    api_key="your_openai_api_key", 
    model="gpt-4o-mini", 
    memory=True
)

# Send a prompt
response = client.prompt("Write a haiku about AI")
print(response)

# Clear conversation history
client.clear_history()
```

### Gemini Integration

```python
from sbai import Gemini

# Initialize with Google API key
client = Gemini(
    api_key="your_google_api_key", 
    model="gemini-2.0-flash-exp", 
    instructions="Be concise and helpful"
)

# Send a prompt
response = client.prompt("Explain quantum computing")
print(response)

# Clear conversation history
client.clear_history()
```

## Configuration Options

### ChatGPT
- `api_key`: Your OpenAI API key (required)
- `model`: OpenAI model to use (default: "gpt-4o-mini")
- `temperature`: Sampling temperature (0-1, default: 0)
- `top_p`: Nucleus sampling parameter (0-1, default: 0)
- `instructions`: System-level instructions
- `max_token`: Maximum tokens in response (default: 200)
- `memory`: Enable conversation memory (default: False)
- `memory_limit`: Maximum messages in memory (default: 5)

### Gemini
- `api_key`: Your Google API key (required)
- `model`: Gemini model to use (default: "gemini-2.0-flash-exp")
- `temperature`: Sampling temperature (0-1, default: 0)
- `top_p`: Nucleus sampling parameter (0-1, default: 0)
- `max_token`: Maximum tokens in response (default: 200)
- `memory`: Enable conversation memory (default: False)
- `instructions`: System-level instructions

## Requirements

- Python 3.8+
- `openai` library
- `google-generativeai` library

## License

MIT License