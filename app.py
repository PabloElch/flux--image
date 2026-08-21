import urllib.parse
import requests
import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Lenchxos AI Studio", page_icon="✨", layout="wide"
)

# Custom Commercial SaaS CSS Injection
st.markdown(
    """
    <style>
    /* Hide standard Streamlit header elements for a clean custom web app feel */
    header {visibility: hidden;}
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 100% !important;
    }
    
    /* Sleek dark theme workspace background */
    .stMain {
        background-color: #0b0f19;
    }

    /* Input card styling */
    div.stTextArea textarea {
        background-color: #111827 !important;
        color: #f3f4f6 !important;
        border: 1px solid #1f2937 !important;
        border-radius: 12px !important;
        padding: 16px !important;
        font-size: 15px !important;
        resize: none;
    }
    div.stTextArea textarea:focus {
        border-color: #6366f1 !important;
        box-shadow: 0 0 0 1px #6366f1 !important;
    }

    /* Primary SaaS Generate Button */
    .stButton button {
        background: linear-gradient(135deg, #6366f1 0%, #4f46e5 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        font-weight: 600 !important;
        height: 52px !important;
        font-size: 16px !important;
        letter-spacing: 0.3px;
        transition: all 0.25s ease;
        box-shadow: 0 4px 12px rgba(99, 102, 241, 0.3);
    }
    .stButton button:hover {
        opacity: 0.9;
        box-shadow: 0 6px 16px rgba(99, 102, 241, 0.5);
    }

    /* Output Canvas Card styling */
    .output-card {
        background-color: #111827;
        border: 1px solid #1f2937;
        border-radius: 16px;
        padding: 24px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);
    }
    </style>
""",
    unsafe_allow_html=True,
)

# App Navigation / Top Bar Header
col_logo, col_badge = st.columns([6, 1])
with col_logo:
  st.markdown(
      "<h3"
      " style='margin:0; font-weight:800; color:#f3f4f6; letter-spacing:-0.5px;'>✨"
      " Lenchxos <span style='color:#6366f1;'>AI Studio</span></h3>",
      unsafe_allow_html=True,
  )
with col_badge:
  st.markdown(
      "<div"
      " style='background:#1f2937; color:#818cf8; padding:6px 12px;"
      " border-radius:20px; font-size:12px; font-weight:600; text-align:center;"
      " border:1px solid #374151;'>FLUX.1 Engine</div>",
      unsafe_allow_html=True,
  )

st.markdown(
    "<hr style='margin-top:10px; margin-bottom:30px; border-color:#1f2937;'>",
    unsafe_allow_html=True,
)

# Professional Split-Pane Layout (Left Control Deck / Right Canvas Output)
control_col, output_col = st.columns([1.1, 1.9], gap="large")

with control_col:
  st.markdown(
      "<h4 style='color:#e5e7eb; font-weight:600; margin-bottom:8px;'>Prompt"
      " Engineering</h4>",
      unsafe_allow_html=True,
  )
  st.markdown(
      "<p style='color:#9ca3af; font-size:13px; margin-bottom:16px;'>Describe"
      " your concept with lighting, subject, and style details for optimal"
      " results.</p>",
      unsafe_allow_html=True,
  )

  # Clean prompt input area
  prompt = st.text_area(
      "Prompt",
      value="",
      placeholder=(
          "A hyper-realistic cinematic portrait of a cyberpunk hacker in a"
          " neon-lit room..."
      ),
      label_visibility="collapsed",
      height=160,
  )

  st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)
  generate_btn = st.button(
      "Generate Masterpiece", type="primary", use_container_width=True
  )

  if generate_btn:
    if not prompt.strip():
      st.warning("Please type a prompt to initialize generation.")
    else:
      # Safe encoding & URL build
      encoded_prompt = urllib.parse.quote(prompt)
      image_url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?model=flux&width=1024&height=1024&enhance=true"
      st.session_state["image_url"] = image_url

with output_col:
  st.markdown(
      "<h4 style='color:#e5e7eb; font-weight:600; margin-bottom:8px;'>Generation"
      " Canvas</h4>",
      unsafe_allow_html=True,
  )

  if "image_url" in st.session_state:
    with st.spinner("Synthesizing neural weights & rendering pixels..."):
      try:
        # Fetch clean image bytes for the studio canvas card
        response = requests.get(st.session_state["image_url"], timeout=15)
        if response.status_code == 200 and len(response.content) > 1000:
          st.image(response.content, use_container_width=True)
          st.markdown("<div style='height: 12px;'></div>", unsafe_allow_html=True)

          # High-end commercial download button styling
          st.download_button(
              label="📥 Download Production Asset (JPEG)",
              data=response.content,
              file_name="lenchxo_flux_masterpiece.jpg",
              mime="image/jpeg",
              use_container_width=True,
          )
        else:
          st.error(
              "The rendering node took too long. Please hit generate again."
          )
      except Exception:
        st.error(
            "Connection timeout with rendering server. Please try again."
        )
  else:
    # Empty placeholder box matching commercial UI design states
    st.markdown(
        """
        <div style="border: 2px dashed #1f2937; border-radius: 16px; height: 420px; display: flex; flex-direction: column; align-items: center; justify-content: center; background-color: #111827; text-align: center; padding: 20px;">
            <div style="font-size: 40px; margin-bottom: 12px;">🎨</div>
            <div style="color: #9ca3af; font-weight: 500; font-size: 15px;">Your canvas is empty</div>
            <div style="color: #4b5563; font-size: 13px; max-width: 260px; margin-top: 6px;">Configure your prompt on the left and click generate to build your asset.</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
