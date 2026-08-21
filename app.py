import streamlit as st

st.set_page_config(
    page_title="Wan 2.1 Custom Video App", page_icon="🎬", layout="wide"
)

st.title("🎬 Wan 2.1 Video Generator (Custom UI)")
st.write(
    "Your custom Streamlit control panel connected to free public generation"
    " nodes."
)

st.info(
    "💡 Note: This approach gives you your own custom-styled web app while"
    " entirely bypassing paid API tokens, serverless key limits, and 402"
    " payment errors."
)

# Embed the official free public Hugging Face Space securely via iframe
st.components.v1.iframe(
    "https://huggingface.co/spaces/Wan-AI/Wan2.1", height=800, scrolling=True
)
