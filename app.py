import streamlit as st

from src.resume_parser import extract_resume_text
from src.resume_analyzer import (
    extract_email,
    extract_phone,
    extract_github,
    extract_linkedin,
    extract_skills,
)
from src.ats_checker import calculate_ats_score

# -------------------------------------------------
# Page Configuration
# -------------------------------------------------

st.set_page_config(
    page_title="AI Career Copilot",
    page_icon="🚀",
    layout="wide",
)

# -------------------------------------------------
# Header
# -------------------------------------------------

st.title("🚀 AI Career Copilot")
st.subheader("Your Personal AI Career Mentor")

st.markdown("---")

# -------------------------------------------------
# Dashboard
# -------------------------------------------------

st.header("📊 Dashboard")

if "ats_score" not in st.session_state:
    st.session_state.ats_score = "--"

if "resume_grade" not in st.session_state:
    st.session_state.resume_grade = "--"

if "skills_found" not in st.session_state:
    st.session_state.skills_found = "--"

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "🎯 ATS Score",
        st.session_state.ats_score
    )

with col2:
    st.metric(
        "🏆 Resume Grade",
        st.session_state.resume_grade
    )

with col3:
    st.metric(
        "🛠 Skills Found",
        st.session_state.skills_found
    )

st.markdown("---")

# -------------------------------------------------
# Features
# -------------------------------------------------

st.header("✨ Features")

left, right = st.columns(2)

with left:
    st.success("📄 Resume Analyzer")
    st.success("🎯 ATS Checker")
    st.success("🧠 Skill Gap Analysis")
    st.success("📚 Learning Roadmap")

with right:
    st.info("🤖 AI Career Mentor")
    st.info("💻 GitHub Analyzer")
    st.info("🎤 Interview Simulator")
    st.info("📊 Career Dashboard")

st.markdown("---")

# -------------------------------------------------
# Resume Upload
# -------------------------------------------------

st.header("📤 Upload Your Resume")

uploaded_file = st.file_uploader(
    "Upload your Resume (PDF or DOCX)",
    type=["pdf", "docx"]
)

# -------------------------------------------------
# Resume Processing
# -------------------------------------------------

if uploaded_file:

    st.success("✅ Resume Uploaded Successfully!")

    resume_text = extract_resume_text(uploaded_file)

    email = extract_email(resume_text)
    phone = extract_phone(resume_text)
    github = extract_github(resume_text)
    linkedin = extract_linkedin(resume_text)
    skills = extract_skills(resume_text)

    ats_result = calculate_ats_score(
    resume_text,
    skills,
    github,
    linkedin
)

    ats_score = ats_result["score"]
    resume_grade = ats_result["grade"]
    ats_breakdown = ats_result["breakdown"]
    strengths = ats_result["strengths"]
    suggestions = ats_result["suggestions"]

    st.session_state.ats_score = f"{ats_score}/100"
    st.session_state.resume_grade = resume_grade
    st.session_state.skills_found = len(skills)
    # ---------------------------------------------
    # Resume Information
    # ---------------------------------------------

    st.markdown("---")

    st.header("📋 Resume Information")

    col1, col2 = st.columns(2)

    with col1:
        st.write("### 📧 Contact")
        st.write(f"**Email:** {email}")
        st.write(f"**Phone:** {phone}")

    with col2:
        st.write("### 🌐 Profiles")
        st.write(f"**GitHub:** {github}")
        st.write(f"**LinkedIn:** {linkedin}")

    # ---------------------------------------------
    # Skills
    # ---------------------------------------------

    st.markdown("---")

    st.header("🛠 Skills Found")

    if skills:

        cols = st.columns(3)

        for index, skill in enumerate(skills):
            cols[index % 3].success(skill)

    else:
        st.warning("No skills detected.")

    # ---------------------------------------------
    # ATS Score
    # ---------------------------------------------

    st.markdown("---")

    st.header("🎯 ATS Score")

    st.progress(ats_score / 100)

    if ats_score >= 85:
        st.success(f"Excellent Resume! ({ats_score}/100)")
    elif ats_score >= 70:
        st.info(f"Good Resume ({ats_score}/100)")
    elif ats_score >= 50:
        st.warning(f"Average Resume ({ats_score}/100)")
    else:
        st.error(f"Needs Improvement ({ats_score}/100)")

    # ---------------------------------------------
    # Suggestions
    # ---------------------------------------------

    st.markdown("---")

    st.header("💡 Improvement Suggestions")

    if suggestions:

        for suggestion in suggestions:
            st.warning(suggestion)

    else:
        st.success("🎉 Your resume looks excellent!")

    # ---------------------------------------------
    # Resume Preview
    # ---------------------------------------------

    st.markdown("---")

    with st.expander("📄 View Extracted Resume Text"):

        st.text_area(
            "Resume Content",
            resume_text,
            height=400,
        )