import streamlit as st
import requests
from PIL import Image

st.set_page_config(page_title="AI ID Fraud Detection", layout="centered")

st.title("AI ID Fraud Detection System")
st.write("Upload an ID image to analyze potential fraud indicators.")

uploaded_file = st.file_uploader("Upload ID Image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:

    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)

    if st.button("Analyze ID"):

        with st.spinner("Analyzing document..."):

            try:

                files = {
                    "file": (uploaded_file.name, uploaded_file.getvalue())
                }

                response = requests.post(
                    "http://127.0.0.1:8000/analyze",
                    files=files
                )

                if response.status_code != 200:
                    st.error("Backend returned error:")
                    st.text(response.text)

                else:

                    result = response.json()

                    st.header("Analysis Results")

                    tamper_text = result["tamper_check"].lower()

                    if "possible" in tamper_text or "detected" in tamper_text:
                        st.error("⚠ Potential Fraud Detected")
                    else:
                        st.success("✓ Document Appears Normal")

                    st.subheader("Tamper Detection")
                    st.write(result["tamper_check"])

                    st.subheader("Fraud Analysis")
                    st.write(result["fraud_report"])

            except Exception as e:
                st.error(f"Error connecting to backend: {e}")

st.markdown("---")

st.markdown("### System Pipeline")
st.markdown("""
Image Upload → Tamper Detection (OpenCV) → OCR (EasyOCR) →  
Vector Retrieval (FAISS) → Fraud Risk Analysis
""")