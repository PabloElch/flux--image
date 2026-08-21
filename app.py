import io
import urllib.parse
import requests
import streamlit as st

# Page configuration
st.set_page_config(page_title="Lenchxos Image Generator", page_icon="🎨")

st.title("🎨 Lenchxos Image Generator")
st.write(
    "Type your prompt below to generate, preview, and download high-resolution"
    " FLUX images."
)

# User prompt input text box
prompt = st.text_area(
    "What do you want to see?",
    (
        "A cute red panda wearing a tiny astronaut helmet, digital art, 8k"
        " resolution"
    ),
)

# Optional quality settings in an expander
with st.expander("Advanced Quality Settings"):
  aspect_ratio = st.selectbox(
      "Aspect Ratio", ["Square (1024x1024)", "Landscape (1280x720)"]
  )
  auto_enhance = st.checkbox(
      "Auto-Enhance Prompt for Better Details", value=True
  )

if st.button("Generate Image", type="primary"):
  if not prompt.strip():
    st.warning("Please type a prompt first.")
  else:
    with st.spinner(
        "Rendering high-quality image with FLUX... Please wait."
    ):
      try:
        # Set dimensions based on user choice
        if "Landscape" in aspect_ratio:
          w, h = 1280, 720
        else:
          w, h = 1024, 1024

        # Encode prompt safely
        encoded_prompt = urllib.parse.quote(prompt)

        # Build URL with enhanced quality parameters
        image_url = f"https://pollinations.ai/p/{encoded_prompt}?model=flux&width={w}&height={h}&enhance={str(auto_enhance).lower()}"

        # Fetch the raw bytes safely from the API
        response = requests.get(image_url)

        if response.status_code == 200 and len(response.content) > 500:
          # Save bytes into session state so it displays and downloads cleanly
          st.session_state["image_bytes"] = response.content
          st.session_state["image_prompt"] = prompt
        else:
          st.error("Failed to generate image bytes. Please try again.")

      except Exception as e:
        st.error(f"An error occurred: {e}")

# If we have generated image bytes stored, display preview and download button
if "image_bytes" in st.session_state:
  st.success("Done!")

  # 1. Preview the image natively inside the app using bytes
  st.image(
      st.session_state["image_bytes"],
      caption=st.session_state["image_prompt"],
      use_container_width=True,
  )

  # 2. Download button that serves a real working JPEG file
  st.download_button(
      label="📥 Download Image",
      data=st.session_state["image_bytes"],
      file_name="lenchxo_flux_image.jpg",
      mime="image/jpeg",
  )
