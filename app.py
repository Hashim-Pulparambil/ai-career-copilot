import streamlit as st
from src.resume_parser import extract_resume_text

st.set_page_config(
    page_title="AI Career Copilot",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 AI Career Copilot")
st.subheader("Your Personal AI Career Mentor")

st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("📄 Resume Score", "--")

with col2:
    st.metric("🎯 ATS Score", "--")

with col3:
    st.metric("💼 Target Role", "--")

st.markdown("---")

st.header("✨ Features")

col1, col2 = st.columns(2)

with col1:
    st.success("📄 Resume Analyzer")
    st.success("🎯 ATS Checker")
    st.success("🧠 Skill Gap Analysis")
    st.success("📚 Learning Roadmap")

with col2:
    st.info("🤖 AI Career Mentor")
    st.info("💻 GitHub Analyzer")
    st.info("🎤 Interview Simulator")
    st.info("📊 Career Dashboard")

st.markdown("---")

st.header("🚀 Get Started")

uploaded_file = st.file_uploader(
    "Upload your Resume (PDF or DOCX)",
    type=["pdf", "docx"]
)

if uploaded_file:
    st.success("Resume uploaded successfully!")

uploaded_file = st.file_uploader(
    "Upload your Resume",
    type=["pdf", "docx"]
)

if uploaded_file:

    st.success("Resume Uploaded Successfully!")

    resume_text = extract_resume_text(uploaded_file)

    st.subheader("Resume Preview")

    st.text_area(
        "Extracted Text",
        resume_text,
        height=400
    )