import urllib.parse
import streamlit as st

# Page configuration
st.set_page_config(page_title="Lenchxos Image Generator", page_icon="🎨")

st.title("🎨 Lenchxos Image Generator")
st.write(
    "Type your prompt below to generate and view high-resolution FLUX"
    " images instantly."
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
    # Set dimensions based on user choice
    if "Landscape" in aspect_ratio:
      w, h = 1280, 720
    else:
      w, h = 1024, 1024

    # Encode prompt safely for the URL
    encoded_prompt = urllib.parse.quote(prompt)

    # Correct updated Pollinations API endpoint format
    image_url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?model=flux&width={w}&height={h}&enhance={str(auto_enhance).lower()}"

    # Save to session state so it stays on screen
    st.session_state["image_url"] = image_url
    st.session_state["image_prompt"] = prompt

# Display image and download options if available
if "image_url" in st.session_state:
  st.success("Done!")

  # 1. Preview the image natively and smoothly
  st.image(
      st.session_state["image_url"],
      caption=st.session_state["image_prompt"],
      use_container_width=True,
  )

  # 2. Clean download action box
  st.markdown("### Save Your Image")
  st.markdown(
      f"👉 **[Click Here to Open Full-Res"
      f" Image]({st.session_state['image_url']})**"
  )
  st.info(
      "Tip: Click the link above to open the clean image file in a new tab,"
      " then right-click and select **'Save image as...'** to download it to"
      " your device."
  )
