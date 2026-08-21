import streamlit as st
from huggingface_hub import InferenceClient

# Page configuration
st.set_page_config(page_title="Lenchxos Image Generator", page_icon="🎨")

st.title("🎨 Lenchxos Image Generator")
st.write("Type your prompt below and generate high-quality open-source images.")

# Hardcoded token in the backend (no prompts or sidebars required)
HF_TOKEN = "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"

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
    with st.spinner("Generating image with FLUX.1 Schnell... Please wait."):
      try:
        # Initialize the API client using your backend token
        client = InferenceClient(provider="auto", api_key=HF_TOKEN)

        # Request the image from FLUX.1 Schnell
        image = client.text_to_image(
            prompt=prompt,
            model="black-forest-labs/FLUX.1-schnell",
        )

        # Display the result
        st.success("Done!")
        st.image(image, caption=prompt, use_container_width=True)

      except Exception as e:
        st.error(f"An error occurred: {e}")
