import urllib.parse
import requests
import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Lenchxos AI Studio", page_icon="✨", layout="centered"
)

# Custom CSS for a sleek, commercial SaaS look
st.markdown(
    """
    <style>
    /* Global styling & font adjustments */
    .main {
        background-color: #0e1117;
    }
    
    /* Rounded text area */
    .stTextArea textarea {
        border-radius: 12px !important;
        border: 1px solid #30363d !important;
        padding: 14px !important;
        font-size: 16px !important;
        background-color: #161b22 !important;
        color: #c9d1d9 !important;
    }
    
    /* Modern primary button */
    .stButton button {
        border-radius: 12px !important;
        font-weight: 600 !important;
        height: 48px !important;
        font-size: 16px !important;
        transition: all 0.2s ease-in-out;
    }
    
    /* Image preview container border */
    .element-container img {
        border-radius: 16px !important;
        box-shadow: 0 8px 24px rgba(0,0,0,0.3);
    }
    </style>
""",
    unsafe_allow_html=True,
)

# Commercial Header Section
st.markdown(
    "<h1"
    " style='text-align: center; font-weight: 800; margin-bottom: 0px;'>✨"
    " Lenchxos AI Studio</h1>",
    unsafe_allow_html=True,
)
st.markdown(
    "<p style='text-align: center; color: #8b949e; margin-bottom: 25px;'>Type"
    " your vision and generate production-grade FLUX.1 assets"
    " instantly.</p>",
    unsafe_allow_html=True,
)

# Centered layout container for the prompt box
prompt = st.text_area(
    "Prompt",
    value="",
    placeholder=(
        "A cinematic hyper-realistic shot of a futuristic cyberpunk city at"
        " night..."
    ),
    label_visibility="collapsed",
)

# Centered generation button layout
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
  generate_btn = st.button("Generate Asset", type="primary", use_container_width=True)

if generate_btn:
  if not prompt.strip():
    st.warning("Please enter a prompt to begin.")
  else:
    with st.spinner("Synthesizing pixels with FLUX.1..."):
      encoded_prompt = urllib.parse.quote(prompt)
      image_url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?model=flux&width=1024&height=1024&enhance=true"
      st.session_state["image_url"] = image_url

# Result Section styled like a professional platform output card
if "image_url" in st.session_state:
  st.markdown("<br>", unsafe_allow_html=True)

  with st.container():
    # Image Preview
    st.image(st.session_state["image_url"], use_container_width=True)
    st.markdown("<br>", unsafe_allow_html=True)

    # Download Action Button
    try:
      response = requests.get(st.session_state["image_url"], timeout=10)
      if response.status_code == 200 and len(response.content) > 1000:
        st.download_button(
            label="📥 Download High-Resolution Image",
            data=response.content,
            file_name="lenchxo_flux_asset.jpg",
            mime="image/jpeg",
            use_container_width=True,
        )
    except Exception:
      st.warning(
          "Could not fetch download payload automatically. Try refreshing."
      )
