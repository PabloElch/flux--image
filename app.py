import urllib.parse
import requests
import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Lenchxos AI Studio", page_icon="✨", layout="wide"
)

# Custom Clean Light Aesthetic CSS Injection
st.markdown(
    """
    <style>
    /* Global Clean Light Theme */
    .stApp {
        background-color: #f8fafc !important;
        color: #0f172a !important;
    }
    
    header {visibility: hidden;}
    .block-container {
        padding-top: 2.5rem;
        padding-bottom: 3rem;
        max-width: 1200px !important;
    }

    /* Input text area card styling */
    div.stTextArea textarea {
        background-color: #ffffff !important;
        color: #0f172a !important;
        border: 1px solid #cbd5e1 !important;
        border-radius: 12px !important;
        padding: 16px !important;
        font-size: 15px !important;
        box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
        resize: none;
    }
    div.stTextArea textarea:focus {
        border-color: #4f46e5 !important;
        box-shadow: 0 0 0 2px rgba(79, 70, 229, 0.15) !important;
    }

    /* Primary SaaS Generate Button */
    .stButton button {
        background: #4f46e5 !important;
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        font-weight: 600 !important;
        height: 50px !important;
        font-size: 15px !important;
        letter-spacing: 0.2px;
        transition: all 0.2s ease;
        box-shadow: 0 4px 12px rgba(79, 70, 229, 0.25);
    }
    .stButton button:hover {
        background: #4338ca !important;
        box-shadow: 0 6px 16px rgba(79, 70, 229, 0.35);
    }

    /* Download button styling alignment */
    div.stDownloadButton button {
        background: #ffffff !important;
        color: #0f172a !important;
        border: 1px solid #cbd5e1 !important;
        border-radius: 12px !important;
        font-weight: 600 !important;
        height: 48px !important;
        transition: all 0.2s ease;
    }
    div.stDownloadButton button:hover {
        background: #f1f5f9 !important;
        border-color: #94a3b8 !important;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# Header Navigation Section
col_logo, col_badge = st.columns([6, 1])
with col_logo:
  st.markdown(
      "<h3"
      " style='margin:0; font-weight:800; color:#0f172a; letter-spacing:-0.5px;'>✨"
      " Lenchxos <span style='color:#4f46e5;'>AI Studio</span></h3>",
      unsafe_allow_html=True,
  )
with col_badge:
  st.markdown(
      "<div"
      " style='background:#e0e7ff; color:#4338ca; padding:6px 12px;"
      " border-radius:20px; font-size:12px; font-weight:600; text-align:center;"
      " border:1px solid #c7d2fe;'>By Lencho Lemessa</div>",
      unsafe_allow_html=True,
  )

st.markdown(
    "<hr style='margin-top:12px; margin-bottom:32px; border-color:#e2e8f0;'>",
    unsafe_allow_html=True,
)

# Split-Pane Workspace (Left Control Deck / Right Canvas Output)
control_col, output_col = st.columns([1.1, 1.9], gap="large")

with control_col:
  st.markdown(
      "<h4 style='color:#1e293b; font-weight:600; margin-bottom:6px;'>Prompt"
      " Studio</h4>",
      unsafe_allow_html=True,
  )
  st.markdown(
      "<p style='color:#64748b; font-size:13px; margin-bottom:16px;'>Type your"
      " concept cleanly. The engine will synthesize your asset.</p>",
      unsafe_allow_html=True,
  )

  # Clean prompt input area
  prompt = st.text_area(
      "Prompt",
      value="",
      placeholder=(
          "A minimalist studio product shot of a futuristic ceramic vase, soft"
          " natural lighting..."
      ),
      label_visibility="collapsed",
      height=170,
  )

  st.markdown("<div style='height: 8px;'></div>", unsafe_allow_html=True)
  generate_btn = st.button(
      "Generate Masterpiece", type="primary", use_container_width=True
  )

  if generate_btn:
    if not prompt.strip():
      st.warning("Please type a prompt to initialize generation.")
    else:
      encoded_prompt = urllib.parse.quote(prompt)
      image_url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?model=flux&width=1024&height=1024&enhance=true"
      st.session_state["image_url"] = image_url

with output_col:
  st.markdown(
      "<h4 style='color:#1e293b; font-weight:600; margin-bottom:6px;'>Live"
      " Canvas</h4>",
      unsafe_allow_html=True,
  )

  if "image_url" in st.session_state:
    with st.spinner("Synthesizing neural weights & rendering pixels..."):
      try:
        response = requests.get(st.session_state["image_url"], timeout=15)
        if response.status_code == 200 and len(response.content) > 1000:
          # Clean container wrapper for image preview
          st.markdown(
              "<div"
              " style='background: #ffffff; padding: 12px; border-radius: 16px;"
              " border: 1px solid #e2e8f0; box-shadow: 0 4px 12px rgba(0,0,0,"
              " 0.04);'>"
              "",
              unsafe_allow_html=True,
          )
          st.image(response.content, use_container_width=True)
          st.markdown("</div>", unsafe_allow_html=True)

          st.markdown("<div style='height: 12px;'></div>", unsafe_allow_html=True)

          st.download_button(
              label="📥 Download Production Asset (.jpg)",
              data=response.content,
              file_name="lenchxo_flux_masterpiece.jpg",
              mime="image/jpeg",
              use_container_width=True,
          )
        else:
          st.error("Server took too long. Please hit generate again.")
      except Exception:
        st.error("Connection timeout with rendering server. Please try again.")
  else:
    # Professional light aesthetic empty state box
    st.markdown(
        """
        <div style="border: 2px dashed #cbd5e1; border-radius: 16px; height: 430px; display: flex; flex-direction: column; align-items: center; justify-content: center; background-color: #ffffff; text-align: center; padding: 20px;">
            <div style="font-size: 36px; margin-bottom: 12px;">🎨</div>
            <div style="color: #334155; font-weight: 600; font-size: 15px;">Workspace Ready</div>
            <div style="color: #64748b; font-size: 13px; max-width: 260px; margin-top: 4px;">Enter a description on the left panel to render your high-resolution asset.</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
      # Sleek Footer Section
st.markdown(
    """
    <hr style='margin-top: 50px; margin-bottom: 20px; border-color: #e2e8f0;'>
    <div style='display: flex; justify-content: space-between; align-items: center; color: #64748b; font-size: 13px; padding-bottom: 20px;'>
        <div>Built by <span style='color: #0f172a; font-weight: 600;'>Lencho Lemessa</span></div>
        <div>Powered by FLUX.1 AI Engine</div>
    </div>
    """,
    unsafe_allow_html=True,
)
