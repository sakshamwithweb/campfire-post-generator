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


# import os
# import requests
# from dotenv import load_dotenv
# load_dotenv()
# headers = {
#     "Authorization": f"Bearer {os.getenv('HACKCLUB_AI_API')}",
#     "Content-Type": "application/json"
# }
# payload = {
#     "model": "x-ai/grok-4.1-fast",
#     "messages": [
#         {
#             "role": "user",
#             "content": "dont you know elon changed his mission from mars to moon lol"
#         }
#     ]
# }
# ask_to_llm = requests.post(
#     os.getenv("HACKCLUB_AI_URL"), headers=headers, json=payload)
# print(ask_to_llm.json()["choices"][0]["message"]["content"])

# a = {'id': 'gen-1773126333-ylabG6jY8sToFfbjRS7a', 'object': 'chat.completion', 'created': 1773126333, 'model': 'x-ai/grok-4.1-fast', 'provider': 'xAI', 'system_fingerprint': None, 'choices': [{'index': 0, 'logprobs': None, 'finish_reason': 'stop', 'native_finish_reason': 'completed', 'message': {'role': 'assistant', 'content': ' {"video_index":"0","start_second":18,"end_second":20,"confidence":1,"reason":"Close-up mid-shot at sec 18-19 shows Winter Soldier\'s metallic arm impacting Cap\'s shield in tense struggle; sec 20 close-up of Cap\'s strained face. Matches fight choreography, metal arm, determined expressions, kinetic camera."}', 'refusal': None, 'reasoning': 'The task is to find which of the 3 videos best matches the sentence: "A close-up action shot from the Captain America: The Winter Soldier or Civil War fight choreography, focusing on Captain America (Chris Evans) and the Winter Soldier (Bucky Barnes). The specific moment should capture a tense, mid-fight confrontation, possibly involving a quick block, a grapple, or a high-intensity exchange of blows. The mood should be serious and combative. Look for dramatic, kinetic camera work typical of MCU fight scenes, preferably at eye level or slightly low angle to emphasize power differentials. Focus on identifiable subject elements: the distinct metal arm of Bucky and Cap\'s determined facial expression."\n\n\n## Examining Video Criteria\n- The task is to identify which of three videos best matches a detailed description of a fight scene from Captain America: The Winter Soldier or Civil War.\n- The description focuses on a close-up, tense confrontation between Captain America (Chris Evans) and the Winter Soldier (Bucky Barnes), with specific actions like a quick block or grapple.\n\n## Analyzing Key Elements\n- Look for identifiable details like Bucky\'s metal arm and Cap\'s determined facial expression to ensure authenticity.\n- The scene should feature dramatic, kinetic camera work, preferably at eye level or low angle, to emphasize power dynamics and intensity.\n\n## Examining Video Criteria\n- Video 0 features extensive fight descriptions, including Captain America and Winter Soldier, with shield interactions, metal arm, and close-up faces, aligning closely with the description.\n- Video 1 focuses on car chases, with less emphasis on superhero fights, making it less relevant.\n- Video 2 mentions fights but centers more on ship interiors and drops, with fewer direct interactions between Cap and Bucky.\n\n## Analyzing Key Elements\n- Video 0 includes dynamic camera angles, grapples, punches, and specific moments like Bucky\'s metal arm and Cap\'s strained expression, matching the combative mood.\n- Notable in Video 0: seconds 16-27 show rifle aiming, shield impact, and close-ups, with transcriptions mentioning "Bucky?" confirming authenticity.\n\n## Identifying Match Range\n- A strong match in Video 0 occurs around seconds 18-20, with mid-shots of Bucky’s metal arm impacting Cap’s shield and close-ups of Cap’s strained face.', 'reasoning_details': [{'type': 'reasoning.summary', 'summary': 'The task is to find which of the 3 videos best matches the sentence: "A close-up action shot from the Captain America: The Winter Soldier or Civil War fight choreography, focusing on Captain America (Chris Evans) and the Winter Soldier (Bucky Barnes). The specific moment should capture a tense, mid-fight confrontation, possibly involving a quick block, a grapple, or a high-intensity exchange of blows. The mood should be serious and combative. Look for dramatic, kinetic camera work typical of MCU fight scenes, preferably at eye level or slightly low angle to emphasize power differentials. Focus on identifiable subject elements: the distinct metal arm of Bucky and Cap\'s determined facial expression."\n\n\n## Examining Video Criteria\n- The task is to identify which of three videos best matches a detailed description of a fight scene from Captain America: The Winter Soldier or Civil War.\n- The description focuses on a close-up, tense confrontation between Captain America (Chris Evans) and the Winter Soldier (Bucky Barnes), with specific actions like a quick block or grapple.\n\n## Analyzing Key Elements\n- Look for identifiable details like Bucky\'s metal arm and Cap\'s determined facial expression to ensure authenticity.\n- The scene should feature dramatic, kinetic camera work, preferably at eye level or low angle, to emphasize power dynamics and intensity.\n\n## Examining Video Criteria\n- Video 0 features extensive fight descriptions, including Captain America and Winter Soldier, with shield interactions, metal arm, and close-up faces, aligning closely with the description.\n- Video 1 focuses on car chases, with less emphasis on superhero fights, making it less relevant.\n- Video 2 mentions fights but centers more on ship interiors and drops, with fewer direct interactions between Cap and Bucky.\n\n## Analyzing Key Elements\n- Video 0 includes dynamic camera angles, grapples, punches, and specific moments like Bucky\'s metal arm and Cap\'s strained expression, matching the combative mood.\n- Notable in Video 0: seconds 16-27 show rifle aiming, shield impact, and close-ups, with transcriptions mentioning "Bucky?" confirming authenticity.\n\n## Identifying Match Range\n- A strong match in Video 0 occurs around seconds 18-20, with mid-shots of Bucky’s metal arm impacting Cap’s shield and close-ups of Cap’s strained face.', 'format': 'xai-responses-v1', 'index': 0}, {'type': 'reasoning.encrypted', 'data': 'JY23p0eb+t+EoC0lNT3QKnMHz/HbQgVbYiZuoO5UmN4BfN8wcJrERv9IZcKLR92VXCbvVQJGF7yeGCYJRRjHIMlgPC1xass8ojRI67mxqY3rCugQx4abvbODPTs/5olJ1h8I2KEEvlrhz4WK7LjQpYuYNnOg6KKd/Iqy/31Psow/SqWjbW0b4esVD44nU2qj+bi/5WNY9nLePf/i9FMm+bqjM9mwHtCNK9dOI5oqdJ5XB5rB+PuCP4dhRq1hz09yHZlfjnqy7egM3Z53V7lyfxYCpDNHaNR4m6wgMSsiqsLU/GjARnq87blD61bhcboEl0qmZm+AIIlkeQAkrznMxDVcuCSQRIuECH/Yng0U9zLLcLD1DK64+2TLoow64dmMqgxErT6uVr86GO+IjrSFnCN3N3Y/0RprcTKuOXTTX3NsqX+6xBzQducpUG3velyWAUOVkoYaSSGgKng6GNsU5CkBHicq8RIN1tCm+k7B1WcVLsPao2V31lteEqQ4BhvqqeAifxGXt1YYrEYj6EtoPCKsVbVSbXGqktpwrT3pYKIO6jAhPyVPxSO4D+yq0GUg/74Hx3h6iiZNiA4aYV4wbp5ikWtAOcD5TDzlpfzRKsgZXgjq3ygCfhUkVmg/nSXLUMCKZTSMJf5nsp/4ivtTIn1CdMrS+5BV6AIF9EZQiQ7rNnxZ5QGZ+HK8WTDFxkv5dyt87U4PBszyqDNkBsfiXlKXG1PhGjh0h9XZP5OzkWbPiESI8Y0D875mm0aekDAmNhneUrAvd1Xr/+nI0JuRgKp3ksYPZSd1yxi6JeVBP+9aXuXCiIOY0UKXnqg7n/YtqGPjcGTgm2EUmQRnvNUkAb5LTr9dPWzukaGPpKpsnQ9bjwnsnymklZJeK562i+4lkOHkmV+X6MB/iCLMC7FZXdDTMV519OZHwZ/GVAiQKdm/9bR3y0fO8YAxWqUXsgOiQLlKVeTEG3CFgKNHCjij+/RWYh1CadMyspacySzdtpATz9sXo/517iDfXOiKbYlHYF2dzfYMDkU5jg62KeggBL0ctzZcP6XSAxXcrw7t9x81qnMCNLERDFnpClAxF60FHX4mEGbvKbP2a7rhVL18/3+oepUJgaAVmrWD5H0UOj0X/GyK0/jE4hrYH2LLnZUeCKl58b7AtQbn8K3Ih3leF7oNqevsTP/Ax0ndoHW9WmWSdIpERztdzr5x6sXZMA9DOWrZ6qFQAo7/lIDVhlUjlpu/h3hCzvzNzV7AWH+wilFqkLS0lykZHWgdHBV7GZLirSA4CyGLzybVjxcrtAQoG1VBXXwwvbpvZUd1aS1NgoamWIe/wzKlAwra8bqvcmwkeILJtyPC+gJgobh0Ka5f7IHIOx46DxHSk1qBESkKuKsbvcmS/7959oZoh9c86aoO4BiSTfNGB3g1kfoEzCmMU0F+uL/P1GHdQ8mXoWBNsZuN/XztXUqquyxlg/RazVnUlQd16TWl/L4A6AxfudxnLWlCvB8h9+iTcatRgJjzkWn34U51+nKQmIFGKymLYipSIw81GaxP9PMkT2Uyh22ZD+3N8ApZIaU/OG+m3mFhczMWsqYqmEbcpvpOUDaJNbYvWpuATRQt657UmbllqGoPj5cWBzNMTLId2dsHy3ZONQCvObZzrQ08aVuFkV5fyjz1zrti4nbGRWoyCuWgO/fmo8JtKSb1Hfg65tPgPuL035MXvNUUXyO7At49NcLcsLi46o36vqAPqdpa80JXH8qQb4jGLCTFIxXMrbnLVHQmyM4k7jTYTWQrIhj8Ugxe62anyZV0nhusUx9ZxN0ZulyR8at2fX3OdWismK5cYyui4uqrOaTDyylkxEFBoPGgPuTJvhyPsQ83zeq9m1F/kqtb0YqBfp41x5O6rJILY06tFkvI56vUMxM879uz5vi5oiVzU5+5koIW3ojdHGV2dXsfVMRXpOIDvQIlYOXpIKZc6kcs6coTwk0XR+E4tQhtqkj4iQoCjNYRliCj2WMMdwrWkp6ohM/MqAcvdnjG0mMJMKEbZAmF7bcW/prTW2LbbP6aVSadz1VTbnlwaaiYRU0e+E/Zj4a4BfGqzLdVHB7mmi/u3rGRqmL3pALGbLLAhayfklBfkzUOBL7AFbkGFtcKMvcXh8x0vqcYao8hyuBdi5tHstc2kUWwdaY+vP3z/UgwlaHAJJRrc+Z08nRPvM+Ozwy3Px1Va8MQk0XAMTsUE7WU6HhrKB7dMd4TiOk+p+2g/cKlQ+ig35zHugJpuWzqHlqnrK/nt4PA2YidTmIrQXawoYdQt90wqIuaurQjHJOZ9+duNAeGqL1elFRYLL1E09Ml2dGQCgeCwH/+1zsM8Eug3NpGNlKzhWJSyS3wqtaPR3OEyBcFNdZQZP3Tz/zBkvXdhtQXHYFFMjaPTy3lgb0EjRxv//6qbSv+fP1cINmde1U/OTg6qXm4Nvuxh9H5qOdiR6OsDWdehVWAoQTGqkVv4Po4phm4rqZjQGOliQkt1wu2fzfzCIrKNNHhs/xV0+hFz7QY6lDX6QnxtB8ajQUSEuZR92QQVmLn5dM7ED4gQsL8+bPyWpHGlgvpCPW2GqpYoFIdTPGvFywrCL/hnZOouBl2jScn9K0WZsRp/+k9aaRRKoc0+1JnlKq4210N6q9U/XNUFlo3B76Yn3rHiitB50Qi6SXnMdGbeQnhHQcENWlkDF5xTHJlGUKgDIHHuwZOtuEOsjUIIQ4VTnunHwpDREKTq2EfhNd575DZVsit07BC+whu3N/st8qat38kB+C35P15iaqCtWZ2zXEZHAf1fV1ss6smi4eEZQb/Wi/DNTxifHHf/itbIc6Z1Vg/08AxlAdZLykiXSFIe+kCKTQgcDm9jo+L6SncN+2HPPu31xJ04ARuSFcgtvro5Bz29HN9jL9I+H/NfouIeXNa8agxe6H28vvHayHyeUpAnZVRX8CZZLrVb0ndmIsmJqomBRs2h6DkYzkeyipLzlwy7ukXSl5MfQ8JdesgE9h0qJsNqBs6z8PxcevIfO3PYo9XeKRM8LjbHyDLB++zckc2NpzF3i6I6ITCNwCfSbybGJEoTYn3F3ovXWh+bsR8G661dA9dPvE4y5EDZeWRm+5xzH8F0FkUupO4qqolHHOi32YXGHuoPG+IColcCGAVQz+BZ1jvbOuLAkdJWdOlhHnvUpST5Ye9COIpR1WZvtm03SNPkujNBtL0VxTrxshEOQ6PlO6J0Zq6lk0ftyZVbkBT1e4WwpsCZ0VE7pTkj2SYuzSJzA61tIzADhFFSMYigyxBfsHx5y+Lzk2Br6vkUWMoSbMd2y4EBL1PDleMPRCE0SCqqXrbPHYsoMpxdrLrXyl/AXNhMRGFJD7ofl8QtRetQqIafuuJmxwupmG8XD29LzUiXS8qFYW/nvOYZDPdQNL5LdjzQTxn6MwYDBN5K4D4a0f4jH2weg1aoHOYqOgHLHZvzcNukvL0GtVXz1iSCN4WEpClF9SM5HeS0yXEbF9hogFhlDicyYmzzmpsg6OyFj3i3+VrsKjg9RWteF14VYNmzAntoSSBpaVudjVMbjOgO4+mTAkweejYWaeTpMW3tZf3HZrUXLGkd5t5wm6+4iZc45k2vgew15ndDAbsC1flTHkIqNvsdf/L0aNYgvj9NdPtESJ6wmMUyUDMeSQt32Et4PhGvLMo7+Of2WXWDWYPrPoXXnewiKgjxy9yuSjlNoZFFhd/hNO3rmHfgyTd4uLfrbK8RQu4IJ0BFm/eIvaDoH1/KDre48ofyqH+g/z3eumgi0c8wJSjwiqiDzBgh4xRl0O65SMVmaPo2Au6qNN4VbGSI63ERRsLRUF2OIsAKO756Crzb+PlCqxkWXP3rvyX5CX3BZnJfN6QWaTnFylvGLQlpQS0ufoQEq16TDPXTQmYRvRoznwq4ZrYdTcOYGVCzQRzhZCeOZJySsYEuqhiteM2z0kZYTiMmsnSA4I83mDXqDbXXTc4DWncmHmsxXbr3UvI4GFuFv7YM/j1rs6UskssMh70ryBDP5k1+cYxJjY7+L3vIWUjSHmLsetctSmNL9CSxK4HT1wp82ARI4mIR9+NIHjB6UwmUkMigyvcUqRADky134DYh8T0v2nBizizXfiUVPT9jLkoExxheOojWX6RSeaDWA4fTriAmXYo55dQGi87tU67hZznAWzOKQQ2sjDNULFNKM6WX42nfnCDuBiTPdVpOBLGknBSXp5AKsVvLXK+PLjr4+lV0ckS1bOiZDEqv5/lRetC8G7JFO00n7R1Su3bljpqZVsRZaCUsPr8E1Ukogohm88E5cMHPSnf3V6JTEBVCVMnh+gjbKzvfu7WacV6Ca9rnp+st2OiWWJ3DVrqkW/pLwdiz0H3CvSHfWIR01EmP1Hao460zR6+TqltU8LGBc9oUlfmlYiIBgciObzLNr8oL5xXvO5lSwxEw3qY6zawDlTkjuJNwMZXBXjZcgEYU8mn2bxwP5ILUYpM/O6sUDy92DARY/d55eebsI4bsDDBfPGL3Wy4qidI7FpDNYQ0JtMQReL0GtGFkugSzj/TKgKMF0nHawTfXjvzyfedLfWXkIt9OfSFE2V5aYRIY/EcuiSfQ+DQxJB/scxsHV56Q5E++3UDp/qtHloCjQ54UpQDTJqww7HvbqkjxAK1EK9HDZxNuIEiGgrPHtlg372qkPIFaCpvDoXRlS7CEoRm56AWCWSo8CfAwico04y2STWRyMWL2Df7MAlv4TKXDmtfPGtkADuJEOx5kgiJ78/h0H19BFZZjhnW5cALNDq60gqQ7vVU/NgvlfzKxSncity5JaeaKXSVrJmmpk5lJuVupSFs5Ewt2kqHIU/orNGw9EqDpMhhomOjbxeyeb3y/wQYY/lHvpQo8B5aMbZYCn0ezWmgyxRZ2S5cujdweAdgQ63Sh8xfDiBydd3Ga8Q6TQUvP8THxCFo+rQhzPVCRIdeO/vOP+Bz4M39RT/3donszHD3FUruJJphQDNhMxv+FTlW57OJ2UtYISFodBHJO7WSVjgeA+kBb2IiAXhp9zFfT4yLP9t1W7RNkyXs2nV+9Ilzxz3zNUfW7Bd/eY4rZDmAIzwgAfptdjuwyAN33vs0fH/Chrj5S+Mf/DJAHBttcwRfDrOp7ZGq7oYLBh1gH0VaKHu9FAKlG3MK4MDAK15FFjjGOFCPY+Xsw8Dgh5kPT5VOU2D3zkzCIMUSnIErH+wgR/9AJ94c6nruTe1JqSiK/bS4HzfTKAOESN56OXJoBmVyXVzhQn14+zX6oNu8+Nm8x4Pxmg0ln0JJuYafYZLS/GBUz2q2Pd8lBqJZxuh8LxseouTpYpd9VkZgqJ0S/yI7ZP9XxImUQh2DsfM1Dg78k8Jp5EeCpfrDwkUoG8KfzXqgwKGqDZoRwZYxV7hdqmioqHyw5FdYa/yedWauI577qR3boNnDCEA5E0mYayfrF5mFhIzR4JzAsCEWZDXv8T2bZcXLorRLJDk8Sgumvvy5JpiOLSVfxoFVmtGQ50nnA4BSX1VMNBBq6OfdNSIyJbNzXjqj27FeVlZNlfGO+DqHwdp6ScTIFR71KacBkbGkJ1KM7uSs95zh2V4xYX9Sl2Ur50+YHFZWi5Z5cVQnfdBv3ot4qgrYaUaBoDliOvmJnVSnIobB/NC0q7+ii/reuAWcw/xK31b+QRS6qRZgxIUV56JNanUNv3QPolD4rf2XxDvBeRZxPIGtRHn6cYfgWd1j6qkxrh7zcx1f9x2KBvzGPDvLdYNtCghbbmWQt2RLDWrKtKwj7c+XWUEqPHY78Sq+91gPfTMJsVDz3CriJznzztbbtZODKw8yn8cbg5653opD9dw7PPYcJR2HUShjr+cA5XNiUZ+w+uWM611D8/AYQFoRtiDsQHnHm61vQBABuPmvtTN273WL4BQd51jK0UDjax9DPOhMywJz5zA/in5lWcssXmM1JKwo7c3OZUOsRVxLejDhT9p5YAxog0U/EyQdXVwdHSk727mEKzrgqO/SOgLabGqzNcppE28DIoMHUdxeWtDbeo8GadLoR3dw1qCHYuz/niBiDQijZhrQJNxuwxCfRYIU+JINWRUrr3G/mvcRoJXOjaZ76hobXWcpbBW3uapMtp9hNShsUUo5chCYZ0E6EBzoONVj4nwt3QiD0EYsfRXukJZ7EaxdI0zunvLrdIMsWC2WGWRm/tOMYPAtBOLUSeUw1mk4PaQ/Nv7m2NEhAjS4Qx8bWm9L1t3A5NHew518sHEDIRv635PFP3hPALgSWzy0t/mdbsmsA4E7moI2RQ+HxlBP8nOOO+wIyNOEMeOKiY1AUkfyXJWHWU+U589kgx2faSwFg8a4vhCB8ZnSst/0kTaKclNB+UA4FOsmatwJ+u01B/dYYC5L7YshpI4OKIdPUDSSMyWpAToZpCkILv8Wskjt+59FTgQ/CGVHZ0EoFAy8kJy9UqPkGWq6YS5cFG/+GXEMVc7Lskk4sa1rCPckYVtEH7vtBvEFrThfTOO8CfOYbIrp8UyBWbDB1UEJ4kHgQ8eh/wFk4Qgon4XnGezu5nUOXuEt/c8xGUtyKj9C3EmRTqbzI/puIlR6xzArJEWgfkguhzRg7rX8moJGHnv1hNeiUvE7Q3xw+ZcSxCzDuLlcENOBwXoFpTkKwdZsi/Sx9tuec7hjbtce6JHfrSg1sC5SYjS1OIrJZo9MnetrCKI7PKHfPl2hZimnG/L85pOFvupFpbHheTVRCNyliJb0kkNGP0Mr/3n7w+kwyK53ERrhbZ4LI6/jeramTzB8ocehDjLZc5F6gMfVEbL+q+FPt2mOsfZt5Gc3cBMWwBjPb/XOcaAHU0Shd1VcEMDbBVOGlSSG5gOJy4B7+24hKpLkuft77ClEWQ', 'format': 'xai-responses-v1', 'id': 'rs_f93119e3-b815-9435-a3ee-225eb7d28ca2', 'index': 1}]}}], 'usage': {'prompt_tokens': 144657, 'completion_tokens': 1249, 'total_tokens': 145906, 'cost': 0.059067, 'is_byok': False, 'prompt_tokens_details': {'cached_tokens': 128, 'cache_write_tokens': 0, 'audio_tokens': 0, 'video_tokens': 0}, 'cost_details': {'upstream_inference_cost': 0.059067, 'upstream_inference_prompt_cost': 0.0289122, 'upstream_inference_completions_cost': 0.0006245}, 'completion_tokens_details': {'reasoning_tokens': 1178, 'image_tokens': 0, 'audio_tokens': 0}}}
# import json
# print(json.dumps(a))

# import json
# print(json.loads("{\"video_index\":\"0\",\"start_second\":18,\"end_second\":20,\"confidence\":1,\"reason\":\"Close-up mid-shot at sec 18-19 shows Winter Soldier's metallic arm impacting Cap's shield in tense struggle; sec 20 close-up of Cap's strained face. Matches fight choreography, metal arm, determined expressions, kinetic camera.\"}"))

# def a():
#     a = 5
#     b = 6
#     c = 9
#     return [a, b, c]
# [a, b, c] = a()
# print(a, b, c)

# from moviepy.editor import *
# clip = VideoFileClip("sample.mp4")
# clip = clip.subclip(0,2)
# clip.write_videofile("a.mp4")