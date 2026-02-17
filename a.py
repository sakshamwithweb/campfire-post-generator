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