from crewai import Agent
from tools import initialize_yt_tool
import os

os.environ["OPENAI_MODEL_NAME"]="gpt-4o-mini-search-preview-2025-03-11"

yt_tool = None

def set_openai_api_key(api_key, youtube_channel=None):
    os.environ["OPENAI_API_KEY"] = api_key
    global yt_tool
    yt_tool = initialize_yt_tool(api_key, youtube_channel)
    if yt_tool and hasattr(blog_researcher, 'tools'):
        blog_researcher.tools = [yt_tool]
    if yt_tool and hasattr(blog_writer, 'tools'):
        blog_writer.tools = [yt_tool]


blog_researcher=Agent(
    role='Blog Researcher from Youtube Videos',
    goal='get the relevant video transcription for the topic {topic} from the provided Yt channel',
    verboe=True,
    memory=True,
    backstory=(
       "Expert in understanding videos in AI Data Science , MAchine Learning And GEN AI and providing suggestion" 
    ),
    tools=[], 
    allow_delegation=True
)


blog_writer=Agent(
    role='Blog Writer',
    goal='Narrate compelling tech stories about the video {topic} from YT video',
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplifying complex topics, you craft"
        "engaging narratives that captivate and educate, bringing new"
        "discoveries to light in an accessible manner."
    ),
    tools=[],
    allow_delegation=False
)