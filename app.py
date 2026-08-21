import urllib.parse
import streamlit as st

# Page configuration
st.set_page_config(page_title="Lenchxos Image Generator", page_icon="🎨")

st.title("🎨 Lenchxos Image Generator")
st.write("Type your prompt below and generate high-quality open-source images.")

# User prompt input text box
prompt = st.text_area(
    "What do you want to see?",
    "A cute red panda wearing a tiny astronaut helmet, digital art",
)

# Generate button
if st.button("Generate Image", type="primary"):
  if not prompt.strip():
    st.warning("Please type a prompt first.")
  else:
    with st.spinner(
        "Generating image with FLUX.1 Schnell... Please wait."
    ):
      try:
        # Encode the prompt safely for the URL query string
        encoded_prompt = urllib.parse.quote(prompt)

        # Direct, reliable URL generation endpoint using FLUX
        image_url = f"https://pollinations.ai/p/{encoded_prompt}?model=flux&width=1024&height=1024"

        # Display the result
        st.success("Done!")
        st.image(image_url, caption=prompt, use_container_width=True)

      except Exception as e:
        st.error(f"An error occurred: {e}")
