import streamlit as st

st.set_page_config(
    page_title="Wan 2.1 Free Video App", page_icon="🎬", layout="wide"
)

st.title("🎬 Wan 2.1 Video Generator (100% Free Edition)")
st.write(
    "Your custom Streamlit frontend linked directly to free public generation"
    " spaces."
)

st.info(
    "💡 Note: Cloud video APIs charge for GPU time and require paid credits."
    " This app embeds the official free public web workspace below so you can"
    " generate videos without spending any money."
)

# Embed the official free public Hugging Face Space via iframe
st.components.v1.iframe(
    "https://huggingface.co/spaces/Wan-AI/Wan2.1", height=800, scrolling=True
)
