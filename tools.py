from langchain.tools import tool
import requests
import datetime
import os
import tempfile
import yt_dlp
import cv2
import numpy as np
import base64
import time


def video_caption_generator(prev_frame_caption, base64_str):
    headers = {
        "Authorization": f"Bearer {os.getenv('HACKCLUB_AI_API')}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "google/gemini-2.5-flash-image",
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "What is this image?"},
                    {
                        "type": "image_url",
                        "image_url": {"url": base64_str}
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

    res = response.json()
    result = res["choices"][0]["message"]["content"]

    return result


"""
    req = requests.get(
        f"https://serpapi.com/search.json?engine=youtube&search_query=visisphere&api_key={os.getenv('SERPAPI_APIKEY')}")
    youtube_results = req.json()
    videos = youtube_results["video_results"]
"""


@tool("video_finder", description="Takes list of dicts, with properties as 'query' needed and 'description' for accurate search in YouTube and returns videos' url")
def video_finder_agent(promptsDict):
    # IN FUTURE YOU MAY WANNA DO SORT 'videos' WITH VECTOR SEARCH PROBABLITY
    with tempfile.TemporaryDirectory() as tmpDir:
        videos = [{"link": "https://www.youtube.com/watch?v=HdnRIHhR5l8"}]
        for index, video in enumerate(videos):
            # !Download video
            url = video['link']
            videoPathBaseName = f"{tmpDir}/{index}"
            videoPathFileName = f"{videoPathBaseName}.mp4"
            yt_dlp_opts = {
                'merge_output_format': 'mp4',
                'quiet': True,
                'noprogress': True,
                "outtmpl": videoPathBaseName
            }
            yt_dlp.YoutubeDL(yt_dlp_opts).download(url)

            # !Extract all infos from video like img, audio and everything and convert into text like transcribe, visual explain etc etc. (Save with timeline)
            # Video: capture and explain 1 frame per second of video
            cap = cv2.VideoCapture(videoPathFileName)
            fps = cap.get(cv2.CAP_PROP_FPS)

            idx = 0
            frame_count = 0

            prev_frame_caption = ""
            while True:
                success, frame = cap.read()
                if not success:
                    break

                # Here we want per second
                if (frame_count % fps == 0):
                    encode_params = [int(cv2.IMWRITE_PNG_COMPRESSION), 9]
                    _, buffer = cv2.imencode('.png', frame, encode_params)
                    b64_bytearr = base64.b64encode(buffer).decode("utf-8")
                    base64_str = f"data:image/png;base64,{b64_bytearr}"
                    # with open(f"tmp/{idx}.txt", "w") as f:
                    #     f.write(base64_str)

                    exp = video_caption_generator(prev_frame_caption, base64_str)

                    # process here
                    idx += 1

                frame_count += 1

            cap.release()

            # Audio: transcribe audio and tell

            # !Save All infos somewhere

            # !Create and Store the vector embedding and search your text.

            # !Wherever you get, send all infos and time and break the loop.

            # print(f"Checked video: {video}", "\n\n")

    return ["https://www.myproxyforyoutube.com/x589Ds"]


tools = [video_finder_agent]
