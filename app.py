import streamlit as st
from huggingface_hub import InferenceClient

st.set_page_config(
    page_title="Wan 2.1 Custom UI", page_icon="🎬", layout="centered"
)

st.title("🎬 Wan 2.1 Custom Video Generator")
st.write("Powered by Streamlit + Free Hugging Face Router")

# Grab Hugging Face token from secrets or input box
if "HF_TOKEN" in st.secrets:
  hf_token = st.secrets["HF_TOKEN"]
else:
  hf_token = st.text_input("Enter your Hugging Face Token:", type="password")

prompt = st.text_input(
    "Enter your video prompt:",
    value="A red sports car driving fast down a coastal highway.",
)

if st.button("Generate Video", type="primary"):
  if not hf_token:
    st.error("Please provide your Hugging Face token.")
  elif not prompt.strip():
    st.warning("Please enter a prompt first.")
  else:
    try:
      with st.status(
          "Connecting to inference provider...", expanded=True
      ) as status:
        st.write("Initializing secure connection...")

        # Use the standard inference client with standard model routing
        client = InferenceClient(token=hf_token)

        st.write("Sending generation task to Wan 2.1...")

        # Call using the specific text-to-video provider task wrapper
        video_data = client.text_to_video(
            prompt=prompt, model="Wan-AI/Wan2.1-T2V-1.3B"
        )

        status.update(
            label="Generation complete!", state="complete", expanded=False
        )

      st.success("Video generated successfully!")
      st.video(video_data)

    except Exception as e:
      # Fallback display if the serverless endpoint is sleeping/cold
      st.error(
          f"Generation error: {e}\n\nNote: If the model endpoint is cold or"
          " experiencing high traffic, free serverless nodes can timeout. Try"
          " clicking generate again in 30 seconds."
      )
