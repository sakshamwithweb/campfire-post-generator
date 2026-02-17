import requests
import os
import prompts
import re
from operator import itemgetter
import yt_dlp

def video_download(yt_video, tmpDir, index):
    try:
        title, link, thumbnail = itemgetter("title", "link", "thumbnail")(yt_video)
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
        timeout=600
    )

    res = response.json()
    result = res["choices"][0]["message"]["content"]

    return result


def format_json_str(txt):
    newTxt = re.sub(" +", " ", txt.replace("\n", ""))
    return newTxt
