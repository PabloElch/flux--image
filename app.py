import urllib.parse
import streamlit as st

st.set_page_config(
    page_title="Custom Free Video Generator", page_icon="🎬", layout="centered"
)

st.title("🎬 Custom AI Video Generator")
st.write("Generate videos instantly through direct URL endpoints—no keys needed.")

prompt = st.text_area(
    "Enter your video prompt:",
    placeholder="A cinematic drone shot over a mountain valley at sunrise...",
)

if st.button("Generate Video", type="primary"):
  if not prompt.strip():
    st.warning("Please enter a prompt first.")
  else:
    with st.spinner("Requesting video generation... (This may take a moment)"):
      # URL-encode the user prompt safely
      encoded_prompt = urllib.parse.quote(prompt)

      # Construct the direct media endpoint URL
      # (Using the free generation endpoint path pattern)
      video_url = f"https://gen.pollinations.ai/video/{encoded_prompt}"

      st.success("Video request processed!")

      # Render the video directly from the returned media stream/URL
      st.video(video_url)

      st.markdown(f"**Direct Media URL:** [Open Video Link]({video_url})")
