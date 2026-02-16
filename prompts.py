
def video_caption(idx, last_caption):
    return f"""
You are analyzing a video at 1 frame per second.

Context:
- This frame occurs at second {idx} of the video.
- Description of the previous frame (1 second earlier): {last_caption}

Task:
Carefully analyze the current frame and describe what is happening.

Instructions:
1. Focus only on what is visually observable in the current frame.
2. Maintain continuity with the previous frame description.
3. Mention changes, motion progression, new objects, or shifts in scene.
4. Be precise and structured.
5. Do NOT hallucinate details that are not visible.

IMP: USE Single Quote Only. No double quote as I am using that in variable

Output:
A clear, concise explanation of the current frame that logically connects with the previous one.
    """
