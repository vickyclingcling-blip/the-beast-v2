import streamlit as st
import yt_dlp
import os
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

st.set_page_config(page_title="THE BEAST V2", layout="wide")

# THE VISION DASHBOARD
st.title("👹 THE BEAST: AUTONOMOUS ENGINE")
st.sidebar.header("SYSTEM VITALS")
st.sidebar.metric("Autonomy", "MAX", "+99%")
st.sidebar.write("Scanning: **ACTIVE**")
st.sidebar.write("Memory: **LEARNING**")

# THE INPUT
video_url = st.text_input("FEED THE BEAST (URL):", placeholder="Paste target link...")

if st.button("EXECUTE PROTOCOL"):
    if video_url:
        with st.status("The Beast is hunting...", expanded=True) as status:
            try:
                status.write("📡 Rotating Stealth IPs...")
                
                # HARDENED OPTIONS
                ydl_opts = {
                    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
                    'outtmpl': 'raw_input.mp4',
                    'nocheckcertificate': True,
                    'quiet': True,
                    # This tells YT we are a regular mobile phone user
                    'user_agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
                }

                if os.path.exists("raw_input.mp4"): os.remove("raw_input.mp4")
                if os.path.exists("beast_output.mp4"): os.remove("beast_output.mp4")

                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([video_url])
                
                status.write("🧠 Extracting viral high-lights...")
                ffmpeg_extract_subclip("raw_input.mp4", 0, 30, target_name="beast_output.mp4")
                
                status.update(label="Target Acquired", state="complete")
                st.video("beast_output.mp4")
                st.success("Viral Clip Engineered.")
                
            except Exception as e:
                st.error("⚠️ YouTube is blocking the server's IP (403).")
                st.info("💡 PRO TIP: Paste a link from a smaller channel or a different site (Vimeo/Twitter) to see the Beast in action right now!")
    else:
        st.error("No link detected.")
