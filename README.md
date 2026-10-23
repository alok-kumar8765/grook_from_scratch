# Grok AI Chat Streamer using xAI API

A simple Python script to stream real-time responses from xAI's **Grok** models using the OpenAI Python SDK configured with xAI's base URL.

## Features

* **Streaming Responses**: Receive and print tokens in real-time as they are generated.
* **OpenAI SDK Integration**: Uses the standard `openai` Python client configured with xAI endpoints (`https://api.x.ai/v1`).
* **Grok Model Support**: Configured to query Grok models (`grok-4.5` or `grok-beta`).

## Prerequisites

* **Python 3.10+**
* An active **xAI API Key** (obtainable from the [xAI Console](https://console.x.ai/)).

## Installation

Install the required Python packages using `pip`:

```bash
pip install openai xai-sdk
```

## Setup & Configuration

1. Get your API key from the xAI developer portal.
2. Either pass your API key directly into the script or set it as an environment variable (recommended):

```bash
export XAI_API_KEY="your-xai-api-key"
```

## Usage

1. Save your Python script (e.g., `app.py`).
2. Run the script:

```bash
python app.py
```

## Code Example

```python
import os
from openai import OpenAI

# Initialize OpenAI client with xAI's base URL
client = OpenAI(
    api_key=os.environ.get("XAI_API_KEY", "YOUR_XAI_API_KEY"),
    base_url="https://api.x.ai/v1"
)

# Request a streaming response
response = client.responses.create(
    model="grok-4.5",
    max_output_tokens=500000,
    reasoning={"effort": "low"},
    stream=True,
    input="What is the python Basics?",
)

# Stream the output directly to the console
for event in response:
    if hasattr(event, "delta") and event.delta:
        print(event.delta, end="", flush=True)
```

> **Note on Typos in Original Snippet**:
> * Corrected `from openai import OpenSI` to `from openai import OpenAI`.
> * Fixed variable name typo `envent.delta` to `event.delta`.

## Available Models

| Model | Description |
| :--- | :--- |
| `grok-beta` / `grok-4.5` | Flagship Grok reasoning and text generation models |
| `grok-vision-beta` | Multimodal model supporting image and text input |

## License

This project is open-source and available under the [MIT License](LICENSE).
