# import requests
# from dotenv import load_dotenv
# import os
# import json
# load_dotenv()
# video_query_req = requests.post(
#     os.getenv("HACKCLUB_AI_URL"),
#     headers={
#         "Authorization": f"Bearer {os.getenv('HACKCLUB_AI_API')}",
#         "Content-Type": "application/json"
#     },
#     json={
#         "model": "google/gemini-2.5-flash-lite-preview-09-2025",
#         "messages": [
#             {
#                 "role": "user",
#                 "content": [
#                     {"type": "text", "text": "*IMP: PLAIN JSON, NO FORMATTING or this: \\n\nMESSAGE: Hello bro!"}
#                 ]
#             },
#         ],
#         "response_format": {
#             "type": "json_schema",
#             "json_schema": {
#                 "name": "messageFormat",
#                 "strict": True,
#                 "schema": {
#                     "type": "object",
#                     "properties": {
#                         "message": {
#                             "type": "string",
#                             "description": "Your response"
#                         },
#                         "mood": {
#                             "type": "string",
#                             "description": "happy or sad"
#                         }
#                     },
#                     "required": ["message", "mood"],
#                     "additionalProperties": False
#                 }
#             }
#         }
#     }
# )
# print(repr(video_query_req.json()["choices"][0]["message"]["content"]))


# --- DIDN'T WORK
# import replicate
# import os
# import replicate
# from dotenv import load_dotenv
# load_dotenv()
# client = replicate.Client(api_token=os.getenv("HACKCLUB_AI_API"), base_url="https://ai.hackclub.com/proxy/v1/replicate")
# output = client.run("minimax/speech-02-turbo", input={
#     "text": "This is a test",
#     "emotion": "angry",
#     "voice_id": "Deep_Voice_Man",
#     "language_boost": "English",
#     "english_normalization": True
# })
# print(output.url)


# ---WORKED
# import requests
# from dotenv import load_dotenv
# import os
# load_dotenv()
# model = "minimax/speech-02-turbo"
# url = f"https://ai.hackclub.com/proxy/v1/replicate/models/{model}/predictions"
# headers = {
#     "Authorization": f"Bearer {os.getenv('HACKCLUB_AI_API')}",
#     "Content-Type": "application/json",
#     "Prefer": "wait"
# }
# data = {
#     "input": {
#         "text": "I am Sak G and I love coding hehehehehe",
#         "emotion": "angry",
#         "voice_id": "Deep_Voice_Man",
#         "language_boost": "English",
#         "english_normalization": True
#     }
# }
# req = requests.post(url, headers=headers, json=data)
# print(req.json()["output"])

# Worked
# import requests
# import os
# from dotenv import load_dotenv
# load_dotenv()
# model = "vaibhavs10/incredibly-fast-whisper:3ab86df6c8f54c11309d4d1f930ac292bad43ace52d10c80d87eb258b3c9f79c"
# url = f"https://ai.hackclub.com/proxy/v1/replicate/models/{model}/predictions"
# headers = {
#     "Authorization": f"Bearer {os.getenv('HACKCLUB_AI_API')}",
#     "Content-Type": "application/json",
#     "Prefer": "wait"
# }
# data = {
#     "input": {
#         "task": "transcribe",
#         "audio": "https://replicate.delivery/xezq/yA5XdQTzM4qLDBG6oqkMtiRqEfGOikAsOwCXjKND8If8recsA/tmpyv58_grj.mp3",
#         "return_timestamps": True
#     }
# }
# req = requests.post(url, headers=headers, json=data)
# print(req.text)


# from ffmpeg import FFmpeg
# ffmpeg = FFmpeg().option("y").input("sample.mp4").output("sample.mp3")
# ffmpeg.execute()