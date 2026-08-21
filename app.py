import io
import urllib.parse
import requests
import streamlit as st

# Page configuration
st.set_page_config(page_title="Lenchxos Image Generator", page_icon="🎨")

st.title("🎨 Lenchxos Image Generator")
st.write(
    "Type your prompt below to generate and download high-resolution FLUX"
    " images."
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

        # Fetch image bytes from the URL so we can display and download it cleanly
        response = requests.get(image_url)
        if response.status_code == 200:
          image_bytes = response.content

          # Display result
          st.success("Done!")
          st.image(image_bytes, caption=prompt, use_container_width=True)

          # Add Download Button
          st.download_button(
              label="📥 Download Image",
              data=image_bytes,
              file_name="generated_flux_image.jpg",
              mime="image/jpeg",
          )
        else:
          st.error("Failed to fetch the image. Please try again.")

      except Exception as e:
        st.error(f"An error occurred: {e}")
