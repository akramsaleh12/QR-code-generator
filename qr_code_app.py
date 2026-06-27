import streamlit as st
import qrcode
from io import BytesIO

st.set_page_config(page_title="QR Code Generator", page_icon="🔗", layout="centered")

# ----------------------------------------------------------------------------
# Custom CSS
# ----------------------------------------------------------------------------
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(160deg, #c7d2fe 0%, #e0e7ff 35%, #f5f3ff 70%, #ffffff 100%);
    }
    .main .block-container {
        max-width: 700px;
        padding-top: 2rem;
        padding-bottom: 6rem;
    }
    .qr-hero {
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .qr-title {
        text-align: center;
        font-size: 2.2rem;
        font-weight: 800;
        color: #1f2937;
        margin-bottom: 0.2rem;
    }
    .qr-subtitle {
        text-align: center;
        color: #6b7280;
        font-size: 1.05rem;
        margin-bottom: 1.8rem;
    }
    div[data-testid="stTextInput"] input {
        border-radius: 10px;
        border: 1px solid #cbd5e1;
        padding: 0.6rem 0.9rem;
    }
    .stButton > button, .stDownloadButton > button {
        width: 100%;
        border-radius: 10px;
        font-weight: 600;
        padding: 0.6rem 0;
        border: none;
        transition: transform 0.15s ease, box-shadow 0.15s ease;
    }
    .stButton > button[kind="primary"] {
        background: linear-gradient(135deg, #6366f1, #4f46e5);
        color: white;
    }
    .stButton > button:hover, .stDownloadButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 14px rgba(79, 70, 229, 0.25);
    }
    div[data-testid="stVerticalBlockBorderWrapper"] {
        background: white;
        border-radius: 18px !important;
        padding: 0.6rem 0.4rem;
        box-shadow: 0 8px 24px rgba(79, 70, 229, 0.12);
        margin-top: 1rem;
    }
    footer {visibility: hidden;}
    .app-footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background: #1f2937;
        color: #e5e7eb;
        text-align: center;
        padding: 0.6rem 0;
        font-size: 0.9rem;
        letter-spacing: 0.3px;
        z-index: 100;
    }
    .app-footer span {
        color: #a5b4fc;
        font-weight: 700;
    }
    section[data-testid="stSidebar"] img {
        border-radius: 50%;
        border: 3px solid #6366f1;
        box-shadow: 0 4px 14px rgba(79, 70, 229, 0.25);
    }
    .profile-name {
        text-align: center;
        font-weight: 700;
        font-size: 1.1rem;
        color: #1f2937;
        margin-top: 0.6rem;
    }
    .profile-role {
        text-align: center;
        font-size: 0.85rem;
        color: #6b7280;
        margin-bottom: 0.5rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ----------------------------------------------------------------------------
# Sidebar profile
# ----------------------------------------------------------------------------
with st.sidebar:
    st.image("assets/ak11.png", width=200)
    st.markdown('<div class="profile-name">Akram Elsayed</div>', unsafe_allow_html=True)
    st.markdown('<div class="profile-name">IT Specialist</div>', unsafe_allow_html=True)
    st.divider()
    st.caption("Generate a QR code for any website in seconds, then download it as a PNG.")

# ----------------------------------------------------------------------------
# Hero illustration (original inline SVG, QR-themed) + title
# ----------------------------------------------------------------------------
st.markdown(
    """
    <div class="qr-hero">
    <svg width="160" height="160" viewBox="0 0 160 160" xmlns="http://www.w3.org/2000/svg">
      <rect x="0" y="0" width="160" height="160" rx="28" fill="#eef2ff"/>
      <rect x="24" y="24" width="36" height="36" rx="4" fill="#4f46e5"/>
      <rect x="32" y="32" width="20" height="20" rx="2" fill="#eef2ff"/>
      <rect x="100" y="24" width="36" height="36" rx="4" fill="#4f46e5"/>
      <rect x="108" y="32" width="20" height="20" rx="2" fill="#eef2ff"/>
      <rect x="24" y="100" width="36" height="36" rx="4" fill="#4f46e5"/>
      <rect x="32" y="108" width="20" height="20" rx="2" fill="#eef2ff"/>
      <rect x="100" y="100" width="14" height="14" rx="2" fill="#6366f1"/>
      <rect x="122" y="100" width="14" height="14" rx="2" fill="#4f46e5"/>
      <rect x="100" y="122" width="14" height="14" rx="2" fill="#4f46e5"/>
      <rect x="122" y="122" width="14" height="14" rx="2" fill="#6366f1"/>
      <rect x="68" y="24" width="10" height="10" fill="#a5b4fc"/>
      <rect x="68" y="44" width="10" height="10" fill="#4f46e5"/>
      <rect x="88" y="24" width="10" height="10" fill="#4f46e5"/>
      <rect x="24" y="68" width="10" height="10" fill="#a5b4fc"/>
      <rect x="44" y="68" width="10" height="10" fill="#4f46e5"/>
      <rect x="68" y="68" width="10" height="10" fill="#6366f1"/>
      <rect x="88" y="68" width="10" height="10" fill="#a5b4fc"/>
      <rect x="68" y="88" width="10" height="10" fill="#4f46e5"/>
    </svg>
    </div>
    <div class="qr-title">Website QR Code Generator</div>
    <div class="qr-subtitle">Enter a website address, generate a QR code, and download it.</div>
    """,
    unsafe_allow_html=True,
)

# --- Input ---
url = st.text_input("Website address", placeholder="https://www.example.com")

# Use session_state so the QR image persists across reruns (e.g. when clicking Download)
if "qr_image_bytes" not in st.session_state:
    st.session_state.qr_image_bytes = None

# --- Step 1: Generate QR on button click ---
if st.button("Generate QR Image", type="primary"):
    if not url.strip():
        st.warning("Please enter a website address first.")
    else:
        # Add scheme if missing, so the QR encodes a valid clickable URL
        clean_url = url.strip()
        if not clean_url.startswith(("http://", "https://")):
            clean_url = "https://" + clean_url

        qr = qrcode.QRCode(
            version=None,  # auto-size
            error_correction=qrcode.constants.ERROR_CORRECT_M,
            box_size=10,
            border=4,
        )
        qr.add_data(clean_url)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")

        # Convert image to bytes for display + download
        buf = BytesIO()
        img.save(buf, format="PNG")
        st.session_state.qr_image_bytes = buf.getvalue()
        st.session_state.qr_url = clean_url

# --- Step 2: Display the QR image ---
if st.session_state.qr_image_bytes:
    with st.container(border=True):
        st.success(f"QR code generated for: {st.session_state.qr_url}")
        st.image(st.session_state.qr_image_bytes, caption=st.session_state.qr_url, width=300)

        # --- Step 3: Download button ---
        st.download_button(
            label="⬇️ Download QR Image",
            data=st.session_state.qr_image_bytes,
            file_name="qr_code.png",
            mime="image/png",
        )

# ----------------------------------------------------------------------------
# Footer
# ----------------------------------------------------------------------------
st.markdown(
    """
    <div class="app-footer">
        🔗 QR Code Generator &nbsp;|&nbsp; Made with ❤️ by <span>Akram Elsayed</span>
    </div>
    """,
    unsafe_allow_html=True,
)
