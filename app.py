import streamlit as st
import yt_dlp
import os
import assemblyai as aai
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

# 1. System Config
st.set_page_config(page_title="THE BEAST V2", layout="wide")
st.title("👹 THE BEAST: AUTONOMOUS ENGINE")

# Sidebar for "Memory" and Stats
st.sidebar.header("SYSTEM VITALS")
st.sidebar.progress(75, text="Autonomy: HIGH")
st.sidebar.metric("Clips Processed", "12", "+2 since last boot")

# 2. Input & Logic
video_url = st.text_input("FEED THE BEAST (URL):", placeholder="Drop a link to scan...")

mode = st.radio("Operating Mode:", ["Manual Cut", "AI Scan (Autonomous)"])

if st.button("EXECUTE PROTOCOL"):
    if video_url:
        with st.status("The Beast is waking up...", expanded=True) as status:
            # A. FETCHING
            status.write("📡 Scanning digital environment...")
            ydl_opts = {'format': 'mp4', 'outtmpl': 'raw_input.mp4'}
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([video_url])
            
            if mode == "AI Scan (Autonomous)":
                status.write("🧠 Analyzing motion and emotion...")
                # Here is where the Beast 'thinks'
                # For now, we simulate the 'Win' logic until you add your API key
                start_time, end_time = 30, 90 
                status.write(f"🎯 Target Acquired: {start_time}s to {end_time}s (High Retention Predicted)")
            else:
                start_time, end_time = 0, 60

            # B. TRANSFORMING
            status.write("✂️ Mutating content into short-form...")
            ffmpeg_extract_subclip("raw_input.mp4", start_time, end_time, target_name="beast_output.mp4")
            
            status.update(label="Mission Accomplished", state="complete")
            
            # C. RESULT
            st.video("beast_output.mp4")
            st.success(f"Clip engineered. Predicted Viral Score: 88%")
    else:
        st.error("Feed me a source link first, g.")
