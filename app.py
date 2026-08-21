import urllib.parse
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

        # Save URL in session state so it renders stably
        st.session_state["image_url"] = image_url
        st.session_state["image_prompt"] = prompt

      except Exception as e:
        st.error(f"An error occurred: {e}")

# Display image preview and direct download link if available
if "image_url" in st.session_state:
  st.success("Done!")

  # 1. Preview directly via URL string (No BytesIO crashing errors)
  st.image(
      st.session_state["image_url"],
      caption=st.session_state["image_prompt"],
      use_container_width=True,
  )

  # 2. Provide a clean link to open and save the full image safely
  st.markdown(
      f"📥 **[Click Here to Open & Download Full-Res"
      f" Image]({st.session_state['image_url']})** (Right-click and select 'Save"
      " image as...')"
  )
