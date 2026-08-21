import urllib.parse
import requests
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
    value="",
    placeholder="Type your creative prompt here...",
)

if st.button("Generate Image", type="primary"):
  if not prompt.strip():
    st.warning("Please type a prompt first.")
  else:
    # Encode prompt safely for the URL
    encoded_prompt = urllib.parse.quote(prompt)
    image_url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?model=flux&width=1024&height=1024&enhance=true"

    # Save to session state so it stays on screen
    st.session_state["image_url"] = image_url
    st.session_state["image_prompt"] = prompt

# Display image and native download button if available
if "image_url" in st.session_state:
  st.success("Done!")

  # 1. Preview the image natively and smoothly
  st.image(
      st.session_state["image_url"],
      caption=st.session_state["image_prompt"],
      use_container_width=True,
  )

  # 2. Native click-and-download button
  try:
    response = requests.get(st.session_state["image_url"], timeout=10)
    if response.status_code == 200 and len(response.content) > 1000:
      st.download_button(
          label="📥 Download Image",
          data=response.content,
          file_name="lenchxo_flux_image.jpg",
          mime="image/jpeg",
      )
  except Exception:
    st.warning(
        "Could not load download button automatically. Try refreshing or"
        " generating again."
    )
