import streamlit as st

st.set_page_config(
    page_title="My Free AI Video Hub", page_icon="🎬", layout="centered"
)

st.title("🎬 My Free AI Video Hub")
st.write(
    "Access open-source video models completely for free via public web spaces."
)

# Create tabs for different free public engines
tab1, tab2 = st.tabs(["Wan 2.1 Space", "LTX Video Space"])

with tab1:
  st.subheader("Wan 2.1 Official Community Space")
  st.write(
    "Alibaba's Wan 2.1 hosted publicly on Hugging Face with free browser"
    " execution."
  )
  st.markdown(
      "[👉 Open Official Wan 2.1 Space in New"
      " Tab](https://huggingface.co/spaces/Wan-AI/Wan2.1)"
  )

  # You can embed the space directly into your Streamlit layout using an iframe component
  st.components.v1.iframe(
      "https://huggingface.co/spaces/Wan-AI/Wan2.1", height=700, scrolling=True
  )

with tab2:
  st.subheader("LTX Video Fast Generator")
  st.write(
      "An alternative open-weights high-speed video model running on free public"
      " infrastructure."
  )
  st.markdown(
      "[👉 Open LTX Video Space](https://huggingface.co/spaces/Lightricks/LTX-Video)"
  )
