import requests

url = "https://api.elevenlabs.io/v1/text-to-speech/ZQe5CZNOzWyzPSCn5a3c/stream"

querystring = {"output_format":"mp3_22050_32"}

payload = {
    "model_id": "eleven_monolingual_v1",
    "text": "hey what's up",
    "voice_settings": {
        "similarity_boost": 1,
        "stability": 1,
        "style": 0,
        "use_speaker_boost": True
    }
}
headers = {
    "xi-api-key": "e09f2bc589719cc0dffd7fab5803885e",
    "Content-Type": "application/json"
}

response = requests.request("POST", url, json=payload, headers=headers, params=querystring)

print(response.text)
