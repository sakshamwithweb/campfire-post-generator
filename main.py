from dotenv import load_dotenv
import os
import requests
import json
import tempfile
import cv2
from tools import video_caption_generator, format_json_str, video_download
import base64

# load stuff
load_dotenv()

# variables
# video_api = os.getenv("MEMORIESAI_API")
idea = '''Winter Soldier vs. Cap fight scene. Caption: "When your bestie signs up for Campfire without telling you."'''
# 1. Manager
# One AI that looks at idea and tells us the video we want with query, sound we want or that pre existed one and any text or other things
main_idea_req = requests.post(
    os.getenv("HACKCLUB_AI_URL"),
    headers={
        "Authorization": f"Bearer {os.getenv('HACKCLUB_AI_API')}",
        "Content-Type": "application/json"
    },
    json={
        "model": "google/gemini-2.5-flash-lite-preview-09-2025",
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "text",
                        "text": f"""I am hosting a game jam for teenagers and for promoting it, I am making reels. Here's today's idea: {idea}. Based strictly on this idea, generate a JSON object with the following structure:\n- "Video": A short, highly effective, and searchable YouTube query (not a sentence, not an explanation). It must be optimized so that when I search it on YouTube and check the top 5 results, I can easily find relevant clips.\n- "Description": A detailed explanation of the exact type of clip we are looking for. Clearly describe the visuals, environment, mood, actions, camera style, subjects, and any important elements so we can later match this description with the clip using vectors.\nReturn only one JSON object containing exactly these keys and their values.\nIMPORTANT: Your response must be strictly valid raw JSON only. Do NOT include any markdown, code blocks, backticks, explanations, comments, headings, or extra text before or after the JSON. Do NOT format it with labels or programming annotations. Output only the JSON object."""}
                ]
            }
        ],
        "response_format": {
            "type": "json_schema",
            "json_schema": {
                    "name": "gameJamReelFormat",
                    "strict": True,
                    "schema": {
                        "type": "object",
                        "properties": {
                            "Video": {
                                "type": "string",
                                "description": "A short, highly effective, and searchable YouTube query. Not a sentence or explanation. Optimized to find relevant clips within top 5 results."
                            },
                            "Description": {
                                "type": "string",
                                "description": "A detailed explanation of the exact clip required, including visuals, environment, mood, actions, camera style, subjects, and important elements for vector-based matching."
                            }
                        },
                        "required": ["Video", "Description"],
                        "additionalProperties": False
                    }
            }
        }
    }
)
main_idea = json.loads(format_json_str(main_idea_req.json()["choices"][0]["message"]["content"]))

# Search the YT with the query and get top 5 videos
yt_req = requests.get(f"https://serpapi.com/search.json?engine=youtube&search_query={main_idea['Video']}&api_key={os.getenv('SERPAPI_APIKEY')}")
youtube_results = yt_req.json()
yt_videos = youtube_results["video_results"][:5]

# Download Videos
with tempfile.TemporaryDirectory() as tmpDir:
    print(tmpDir)
    for index, yt_video in enumerate(yt_videos):
        videoPathBaseName, videoPathFileName = video_download(yt_video,tmpDir,index)

# Extract and store visual explanation and transcription of video
# A. Visual Explanations
        cap = cv2.VideoCapture(videoPathFileName)
        fps = int(round(cap.get(cv2.CAP_PROP_FPS)))
        idx = 0
        frame_count = 0
        captions = []
        while True:
            success, frame = cap.read()
            if not success:
                break
            if (frame_count % fps == 0):
                encode_params = [int(cv2.IMWRITE_PNG_COMPRESSION), 9]
                _, buffer = cv2.imencode('.png', frame, encode_params)
                b64_bytearr = base64.b64encode(buffer).decode("utf-8")
                base64_str = f"data:image/png;base64,{b64_bytearr}"

                last_caption = captions[-1] if len(captions) > 0 else ""
                exp = video_caption_generator(last_caption, idx, base64_str)
                captions.append(exp)
                print(f"{idx} done")
                idx += 1
            frame_count += 1
        cap.release()
        with open(f"captions/caption{index}.json", "w") as f:
            f.write(f"""{json.dumps(captions)}""")

# B. Transcription of video
        # print("here")

# Search if the video has that clip, if yes go next or else repeat loop with next video

# Find the time and extract that specific clip from video

# 2. Audio