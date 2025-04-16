from crewai_tools import YoutubeChannelSearchTool
import os

def initialize_yt_tool(api_key=None, youtube_channel=None):
    if api_key:
        os.environ["OPENAI_API_KEY"] = api_key
    
    channel = youtube_channel if youtube_channel else '@freecodecamp'
    return YoutubeChannelSearchTool(youtube_channel_handle=channel)

yt_tool = None

