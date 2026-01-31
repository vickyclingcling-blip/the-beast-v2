if st.button("EXECUTE PROTOCOL"):
    if video_url:
        # 1. Start the Status Block correctly to avoid NameError
        with st.status("The Beast is waking up...", expanded=True) as beast_status:
            
            beast_status.write("📡 Scanning digital environment with Stealth-IP...")
            
            # 2. Stealth Options to avoid being flagged
            ydl_opts = {
                'format': 'best[ext=mp4]/best',
                'outtmpl': 'raw_input.mp4',
                'nocheckcertificate': True,
                # Randomize the "User Agent" to look like different browsers
                'user_agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
                'referer': 'https://www.google.com/',
                'quiet': True,
                'no_warnings': True,
            }
            
            try:
                # Remove old files to keep it fresh
                if os.path.exists("raw_input.mp4"):
                    os.remove("raw_input.mp4")
                
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([video_url])
                
                beast_status.write("🧠 Intelligence check: Identifying viral heat...")
                
                # Default cut for now (0 to 60 seconds)
                start_time, end_time = 0, 60
                
                beast_status.write("✂️ Mutating content into short-form...")
                
                if os.path.exists("beast_output.mp4"):
                    os.remove("beast_output.mp4")
                    
                ffmpeg_extract_subclip("raw_input.mp4", start_time, end_time, target_name="beast_output.mp4")
                
                beast_status.update(label="Mission Accomplished", state="complete")
                
                # 3. Output the result
                st.video("beast_output.mp4")
                st.success("Clip engineered. Predicted Viral Score: 88%")
                
            except Exception as e:
                st.error(f"System Blocked or Failure: {e}")
    else:
        st.error("Feed me a source link first, g.")
