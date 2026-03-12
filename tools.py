import requests
import os
import prompts
import re
from operator import itemgetter
import yt_dlp
import json


def video_download(yt_video, tmpDir, index):
    try:
        title, link, thumbnail = itemgetter(
            "title", "link", "thumbnail")(yt_video)
        videoPathBaseName = f"{tmpDir}/{index}"
        videoPathFileName = f"{videoPathBaseName}.mp4"
        yt_dlp_opts = {
            'format': 'bv*[vcodec^=avc1]+ba/b[vcodec^=avc1]',
            'merge_output_format': 'mp4',
            'quiet': True,
            'noprogress': True,
            'outtmpl': videoPathBaseName
        }
        yt_dlp.YoutubeDL(yt_dlp_opts).download(link)

        return [videoPathBaseName, videoPathFileName]
    except Exception as e:
        print(f"{idx} video failed, retrying..")
        video_download(yt_video, tmpDir, index)


def video_caption_generator(last_caption, idx, base64_str):
    try:
        headers = {
            "Authorization": f"Bearer {os.getenv('HACKCLUB_AI_API')}",
            "Content-Type": "application/json"
        }

        prompt = prompts.video_caption(idx, last_caption)

        payload = {
            "model": "google/gemini-2.5-flash-image",
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt},
                        {
                            "type": "image_url",
                            "image_url": {"url": base64_str}
                        }
                    ]
                }
            ]
        }

        response = requests.post(
            os.getenv("HACKCLUB_AI_URL"),
            headers=headers,
            json=payload,
            timeout=1200
        )
        res = response.json()
        result = res["choices"][0]["message"]["content"]
        return result
    except:
        return video_caption_generator(last_caption, idx, base64_str)


def select_correct_video(target_sentence, videos_infos):
    print(target_sentence)
    headers = {
        "Authorization": f"Bearer {os.getenv('HACKCLUB_AI_API')}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "x-ai/grok-4.1-fast",
        "messages": [
            {
                "role": "user",
                "content": f"""
You are given analysis of 3 videos. Each video contains:
- frame-by-frame visual descriptions
- transcription

Task:
Determine which video best matches the following sentence and identify the exact time range where the match occurs.

Sentence:
{target_sentence}

Video Data:
{json.dumps(videos_infos, indent=2)}

Instructions:
1. Compare the sentence with BOTH the transcription and visual descriptions.
2. Determine which video matches the sentence most closely.
3. Identify the approximate start and end time (in seconds).
4. The detected segment must be **at least 15 seconds long and at most 30 seconds long**.
5. Use only evidence present in the provided data.
6. If no video matches, return video_index = null.
"""
            }
        ],
        "response_format": {
            "type": "json_schema",
            "json_schema": {
                "name": "video_analyzing",
                "schema": {
                    "type": "object",
                    "properties": {
                        "video_index": {"type": "string", "description": "Starts from 0"},
                        "start_second": {"type": "integer"},
                        "end_second": {"type": "integer"},
                        "confidence": {"type": "integer", "description": "Between 0 and 1"},
                        "reason": {"type": "string", "description": "short explanation"}
                    },
                    "required": ["video_index", "start_second", "end_second"]
                }
            }
        }
    }

    ask_to_llm = requests.post(
        os.getenv("HACKCLUB_AI_URL"), headers=headers, json=payload)
    result = json.loads(ask_to_llm.json()["choices"][0]["message"]["content"])

    # Find the time and extract that specific clip from video
    video_index, start_second, end_second = itemgetter(
        "video_index", "start_second", "end_second")(result)

    return [video_index, start_second, end_second]


def format_json_str(txt):
    newTxt = re.sub(" +", " ", txt.replace("\n", ""))
    return newTxt
