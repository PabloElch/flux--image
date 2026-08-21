import streamlit as st

st.set_page_config(
    page_title="Wan 2.1 Free Video App", page_icon="🎬", layout="wide"
)

st.title("🎬 Wan 2.1 Video Generator (Free Edition)")
st.write(
    "Your custom Streamlit interface connected directly to free public"
    " generation spaces."
)

# Create a clean layout with direct access to the free public space
st.info(
    "💡 Note: Cloud video APIs charge for GPU time. This app uses the official"
    " free public web interface embedded directly below so you never spend a"
    " dime."
)

# Embed the official free public Hugging Face Space via iframe
st.components.v1.iframe(
    "https://huggingface.co/spaces/Wan-AI/Wan2.1", height=800, scrolling=True
)
