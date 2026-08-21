import urllib.parse
import streamlit as st

# Page configuration
st.set_page_config(page_title="Lenchxos Image Generator", page_icon="🎨")

st.title("🎨 Lenchxos Image Generator")
st.write("Type your prompt below to generate high-resolution FLUX images.")

# User prompt input text box
prompt = st.text_area(
    "What do you want to see?",
    (
        "A hyper-realistic cinematic shot of a futuristic cyberpunk street"
        " market at night, neon reflections in puddles, 8k resolution"
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

        # Display result
        st.success("Done!")
        st.image(image_url, caption=prompt, use_container_width=True)

      except Exception as e:
        st.error(f"An error occurred: {e}")
