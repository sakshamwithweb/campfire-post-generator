from langchain.tools import tool
import requests
import datetime
import os
import tempfile
import yt_dlp
import cv2
import numpy as np
import base64

"""
    req = requests.get(
        f"https://serpapi.com/search.json?engine=youtube&search_query=visisphere&api_key={os.getenv('SERPAPI_APIKEY')}")
    youtube_results = req.json()
    videos = youtube_results["video_results"]
"""


def video_caption_generator(prev_frame_caption, base64_video):
    prompt = "What is this image?"

    headers = {
        "Authorization": f"Bearer {os.getenv('HACKCLUB_AI_API')}",
        "Content-Type": "application/json"
    }

    base64_image = base64_video.decode("utf-8")

    with open("abc.txt","w") as f:
        f.write(f"data:image/jpeg;base64,{base64_image}")

    payload = {
        "model": "google/gemini-2.5-flash-image",
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
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

    print(result)


@tool("video_finder", description="Takes list of dicts, with properties as 'query' needed and 'description' for accurate search in YouTube and returns videos' url")
def video_finder_agent(promptsDict):

    # IN FUTURE YOU MAY WANNA DO SORT 'videos' WITH VECTOR SEARCH PROBABLITY
    with tempfile.TemporaryDirectory() as tmpDir:
        # print(tmpDir)
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
            # Video: capture and explain 2 frames per second of video
            cap = cv2.VideoCapture(videoPathFileName)
            idx = 0
            prev_frame_caption = ""
            while True:
                success, frame = cap.read()
                if success:
                    # cv2.imshow(str(idx), frame)

                    # HERE PROCESS IMAGE
                    video_caption_generator(
                        prev_frame_caption, base64.b64encode(frame))

                    cv2.waitKey(0) # 100
                    # cv2.destroyWindow(str(idx))
                else:
                    break
                idx += 1
            print("end")

            # Audio: transcribe audio and tell

            # !Save All infos somewhere

            # !Create and Store the vector embedding and search your text.

            # !Wherever you get, send all infos and time and break the loop.

            # print(f"Checked video: {video}", "\n\n")

    return ["https://www.myproxyforyoutube.com/x589Ds"]


tools = [video_finder_agent]
