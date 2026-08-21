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

if st.button("Generate Image", type="primary"):
  if not prompt.strip():
    st.warning("Please type a prompt first.")
  else:
    # Encode prompt safely for the URL (defaulting to clean 1024x1024 with enhance enabled)
    encoded_prompt = urllib.parse.quote(prompt)
    image_url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?model=flux&width=1024&height=1024&enhance=true"

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

  # 2. Clean download instructions
  st.markdown(
      f"👉 **[Click Here to Open Full-Res"
      f" Image]({st.session_state['image_url']})**"
  )
  st.info(
      "Tip: Click the link above to open the clean image file, then right-click"
      " and select **'Save image as...'** to save it to your device."
  )
