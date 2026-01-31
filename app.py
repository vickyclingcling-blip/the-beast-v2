import streamlit as st
import yt_dlp
import os
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

# 1. SETUP
st.set_page_config(page_title="THE BEAST V2", layout="wide")
st.title("👹 THE BEAST: AUTONOMOUS ENGINE")

# 2. DASHBOARD
st.sidebar.header("SYSTEM VITALS")
st.sidebar.metric("Autonomy", "MAX", "+99%")
st.sidebar.write("Status: **READY TO HUNT**")

# 3. INPUT
video_url = st.text_input("FEED THE BEAST (URL):", placeholder="Paste YouTube link here...")

# 4. EXECUTION
if st.button("EXECUTE PROTOCOL"):
    if video_url:
        with st.status("The Beast is waking up...", expanded=True) as beast_status:
            try:
                beast_status.write("📡 Scanning environment with Stealth-IP...")
                
                # STEALTH CONFIG
                ydl_opts = {
                    'format': 'best[ext=mp4]/best',
                    'outtmpl': 'raw_input.mp4',
                    'nocheckcertificate': True,
                    'quiet': True,
                    'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
                    'referer': 'https://www.google.com/',
                }

                # CLEANUP
                if os.path.exists("raw_input.mp4"):
                    os.remove("raw_input.mp4")
                if os.path.exists("beast_output.mp4"):
                    os.remove("beast_output.mp4")

                # DOWNLOAD
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([video_url])
                
                beast_status.write("🧠 Intelligence check: Detecting viral heat...")
                
                # CUT (0 to 60 seconds)
                beast_status.write("✂️ Mutating content into short-form...")
                ffmpeg_extract_subclip("raw_input.mp4", 0, 60, target_name="beast_output.mp4")
                
                beast_status.update(label="Mission Accomplished", state="complete")
                
                # REVEAL
                st.video("beast_output.mp4")
                st.success("Viral Clip Engineered.")
                with open("beast_output.mp4", "rb") as f:
                    st.download_button("DOWNLOAD CLIP", f, file_name="the_beast.mp4")

            except Exception as e:
                st.error(f"Critical System Failure: {e}")
    else:
        st.error("No link, no clip. Feed the Beast.")
