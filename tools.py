from langchain.tools import tool
import requests
import datetime

@tool
def get_time():
    """Get current time in this format: hh:mm:ss"""
    time = datetime.datetime.now()
    return f"{time.hour}:{time.minute}:{time.second}"

@tool
def product_listed_length():
    """Number of products listed on user's site"""
    req = requests.get("https://fakestoreapi.com/products")
    return len(req.json())

tools = [get_time,product_listed_length]