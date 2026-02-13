import requests
from dotenv import load_dotenv
import os
import base64

load_dotenv()

headers = {
    "Authorization": f"Bearer {os.getenv('HACKCLUB_AI_API')}",
    "Content-Type": "application/json"
}

image_url = "https://goo.gle/instrument-img"
image_bytes = requests.get(image_url).content
base64_image = base64.b64encode(image_bytes).decode("utf-8")

payload = {
    "model": "google/gemini-2.5-flash-image",
    "messages": [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "What is this image?"},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{base64_image}"
                    }
                }
            ]
        }
    ]
}

response = requests.post(
    "https://ai.hackclub.com/proxy/v1/chat/completions",
    headers=headers,
    json=payload
)

result = response.json()

with open("def.txt","w") as f:
    f.write(f"data:image/jpeg;base64,{base64_image}")