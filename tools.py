from langchain.tools import tool
import requests
import datetime
import os
import tempfile
import yt_dlp

# 'format': 'bestvideo+bestaudio/best'


@tool("video_finder", description="Takes list of dicts, with properties as 'query' needed and 'description' for accurate search in YouTube and returns videos' url")
def video_finder_agent(promptsDict):
    req = requests.get(
        f"https://serpapi.com/search.json?engine=youtube&search_query=visisphere&api_key={os.getenv('SERPAPI_APIKEY')}")

    youtube_results = req.json()
    videos = youtube_results["video_results"]
    # IN FUTURE YOU MAY WANNA DO SORT 'videos' WITH VECTOR SEARCH PROBABLITY
    with tempfile.TemporaryDirectory() as tmpDir:
        for index, video in enumerate(videos):
            # print(f"checked video: {video}")
            # Download video
            url = "https://www.youtube.com/watch?v=HdnRIHhR5l8"
            # , 'paths': {'home':tmpDir}
            yt_dlp_opts = {
                'merge_output_format': 'mp4',
                "outtmpl": f"{tmpDir}/{index}"
            }
            yt_dlp.YoutubeDL(yt_dlp_opts).download(url)
            print(os.listdir(tmpDir))

        # Extract all infos from video like img, audio and everything and convert into text like transcribe, visual explain etc etc

        
        # Make a vector embedding and search your text.
        # wherever you get, send all infos and time and break the loop.
        # print(f"Checked video: {video}", "\n\n")

    return ["https://www.myproxyforyoutube.com/x589Ds"]


tools = [video_finder_agent]
