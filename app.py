##========================
## Requirements :
## Python 3.10+ version
## pip install xai-sdk openai
##========================

#from xai_sdk import Client
#from xai_sdk.chat import user
from openai import OpenSI

#client = Client(api_key="")
client = OpenAI(api_key="",base_url="https://api.x.ai/v1")
response = client.responses.create(
	model = "grok-4.5",
	max_output_tokens=500000,
	reasoning ={"effort":"low"},
	stream =True,
	input = "What is the python Basics?",
	)
for event in response:
	if hasattr(event,"delta") and envent.delta:
		print(envent.delta,end="",flush=True)