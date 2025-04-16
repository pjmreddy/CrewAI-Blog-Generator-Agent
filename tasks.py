from crewai import Task
from agents import blog_researcher, blog_writer, yt_tool


research_task = Task(
  description=(
    "Identify the video {topic}."
    "Get detailed information about the video from the channel video."
  ),
  expected_output='A comprehensive 3 paragraphs long report based on the {topic} of video content.',
  agent=blog_researcher,
)


write_task = Task(
  description=(
    "get the info from the youtube channel on the topic {topic}."
  ),
  expected_output='Summarize the info from the youtube channel video on the topic{topic} and create the content for the blog',
  agent=blog_writer,
  async_execution=False,
  output_file='new-blog-post.md' 
)
