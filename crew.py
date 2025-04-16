from crewai import Crew,Process
from agents import blog_researcher,blog_writer, set_openai_api_key
from tasks import research_task,write_task


def run_crew(api_key, topic, youtube_channel=None):
  
    set_openai_api_key(api_key, youtube_channel)
    
    crew = Crew(
      agents=[blog_researcher, blog_writer],
      tasks=[research_task, write_task],
      process=Process.sequential,  
      memory=True,
      cache=True,
      max_rpm=100,
      share_crew=True
    )
    
    result = crew.kickoff(inputs={'topic': topic})
    return result

if __name__ == "__main__":
    result = run_crew("your-api-key-here", 'AI VS ML VS DL vs Data Science')
    print(result)