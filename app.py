import sys
import pysqlite3 as sqlite3

sys.modules['sqlite3'] = sqlite3

import streamlit as st
import os
import time
from crew import run_crew


st.set_page_config(page_title="CrewAI Blog Generator", layout="wide")


st.title("CrewAI Blog Generator")
st.markdown("""
This application uses CrewAI to generate blog content based on YouTube videos.
Provide your OpenAI API key, a topic, and optionally a YouTube channel handle to generate a blog post.
""")


with st.sidebar:
    st.header("Configuration")
    api_key = st.text_input("Enter your OpenAI API Key", type="password", help="Your API key will not be stored")
    st.markdown("""**Note:** This application requires an OpenAI API key with access to GPT-4.""")


topic = st.text_input("Enter a topic for your blog post", value="AI VS ML VS DL vs Data Science", 
                     help="The topic to search for in YouTube videos")


youtube_channel = st.text_input("Enter YouTube channel handle (optional)", value="@freecodecamp",
                              help="Enter a YouTube channel handle (e.g., @freecodecamp). If left as default, freeCodeCamp channel will be used.")


if st.button("Generate Blog", type="primary", disabled=not api_key):
    if not api_key:
        st.error("Please enter your OpenAI API key")
    else:
        try:
           
            progress_placeholder = st.empty()
            blog_placeholder = st.empty()
            
            with st.spinner("CrewAI is working on your blog post..."):
                progress_placeholder.info("Step 1/2: Researching YouTube videos on the topic...")
            
                result = run_crew(api_key, topic, youtube_channel)
                
              
                progress_placeholder.success("Blog post generated successfully!")
                
            
                blog_placeholder.markdown("## Generated Blog Post")
                blog_placeholder.markdown(result)
                
             
                if os.path.exists("new-blog-post.md"):
                    with open("new-blog-post.md", "r") as f:
                        blog_content = f.read()
                    st.download_button(
                        label="Download Blog Post",
                        data=blog_content,
                        file_name="blog-post.md",
                        mime="text/markdown"
                    )
                
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
            st.info("Please check your API key and try again.")


with st.expander("How to use this application"):
    st.markdown("""
    1. Enter your OpenAI API key in the sidebar
    2. Enter a topic for your blog post
    3. Click 'Generate Blog' and wait for the results
    4. Download the generated blog post if desired
    
    The application uses CrewAI to:
    - Research YouTube videos on your topic from the specified YouTube channel (defaults to freeCodeCamp if none provided)
    - Generate a comprehensive blog post based on the video content
    """)
