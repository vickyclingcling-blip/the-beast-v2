import streamlit as st
import yt_dlp
import os
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

st.set_page_config(page_title="THE BEAST", page_icon="👹")
st.title("👹 THE BEAST V1")

video_url = st.text_input("Paste YouTube Link:")
start = st.number_input("Start Second", value=0)
end = st.number_input("End Second", value=30)

if st.button("ACTIVATE BEAST"):
    with st.spinner('Hunting for clips...'):
        try:
            # Download logic
            ydl_opts = {'format': 'mp4', 'outtmpl': 'vid.mp4'}
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([video_url])

            # Cut logic
            ffmpeg_extract_subclip("vid.mp4", start, end, target_name="clip.mp4")

            # Show results
            st.video("clip.mp4")
            with open("clip.mp4", "rb") as f:
                st.download_button("Download Viral Clip", f, file_name="beast.mp4")
        except Exception as e:
            st.error(f"Error: {e}")
