import tempfile
import time
from pathlib import Path

import numpy as np
import streamlit as st
from PIL import Image

# Optional imports guarded so the app still runs if ultralytics isn't available
try:
    from ultralytics import YOLO
    _HAVE_YOLO = True
except Exception:
    YOLO = None
    _HAVE_YOLO = False

# ----------- UI SETUP -----------
st.set_page_config(page_title="AI Crop Detect Demo", page_icon="🌾", layout="wide")
st.title("🌾 AI Crop Detect – Streamlit Demo")

st.sidebar.header("Settings")
mode = st.sidebar.selectbox(
    "Detection Mode",
    ["YOLO Object Detection (recommended)", "Green Vegetation Mask (quick demo)"],
)

st.sidebar.markdown("---")
source_type = st.sidebar.radio("Input Type", ["Image", "Video"], horizontal=True)

uploaded_weights = None
if mode.startswith("YOLO"):
    st.sidebar.subheader("YOLO Weights")
    uploaded_weights = st.sidebar.file_uploader(
        "Upload your crop-trained YOLOv8/v9 .pt file (optional)",
        type=["pt"],
        accept_multiple_files=False
    )
    use_default = st.sidebar.checkbox("Use default yolov8n.pt if none uploaded", value=True)

st.sidebar.markdown("---")
conf_thres = st.sidebar.slider("Confidence Threshold", 0.1, 0.9, 0.25, 0.05)
iou_thres = st.sidebar.slider("IoU Threshold (NMS)", 0.1, 0.9, 0.45, 0.05)

# ----------- HELP TEXT -----------
with st.expander("How this works", expanded=False):
    st.markdown(
        """
- **YOLO Object Detection**: Load your own crop-detection weights (`.pt`). If you don't upload any and keep the checkbox on, the app uses `yolov8n.pt` (generic COCO model) for demonstration.
- **Green Vegetation Mask**: A fast, classical HSV threshold to highlight green pixels. It's not a trained model but useful as a quick vegetation proxy.
        """
    )

# ----------- INPUT -----------
if source_type == "Image":
    up = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png", "bmp", "webp"])
    cam = st.camera_input("Or take a photo")
    image_input = up or cam

elif source_type == "Video":
    video_file = st.file_uploader("Upload a video", type=["mp4", "mov", "avi", "mkv"])
    image_input = video_file

# ----------- HELPERS -----------
def load_image_to_array(file) -> np.ndarray:
    img = Image.open(file).convert("RGB")
    return np.array(img)

def ensure_yolo_model():
    """
    Returns a YOLO model, either from uploaded weights or default yolov8n.pt.
    """
    if not _HAVE_YOLO:
        st.error("Ultralytics is not installed. Check requirements and restart.")
        st.stop()

    weights_path = None
    if uploaded_weights is not None:
        # Save uploaded weights to a temp file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pt") as tmp:
            tmp.write(uploaded_weights.read())
            weights_path = tmp.name
    elif use_default:
        weights_path = "yolov8n.pt"  # generic model

    if weights_path is None:
        st.warning("Please upload crop-trained weights (.pt) or enable default yolov8n.pt.")
        st.stop()

    try:
        model = YOLO(weights_path)
    except Exception as e:
        st.error(f"Failed to load YOLO weights: {e}")
        st.stop()

    return model

def draw_legend(canvas, items):
    """Simple legend drawer for Streamlit images."""
    import cv2
    x, y = 10, 10
    for text in items:
        cv2.rectangle(canvas, (x-5, y-20), (x + 200, y + 10), (0, 0, 0), -1)
        cv2.putText(canvas, text, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 1, cv2.LINE_AA)
        y += 30
