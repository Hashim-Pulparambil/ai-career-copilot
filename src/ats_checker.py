import re


def calculate_ats_score(resume_text, skills, github, linkedin):

    score = 0

    suggestions = []

    # ------------------------
    # Contact Information
    # ------------------------

    email_pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

    phone_pattern = r"(\+?\d[\d\s-]{8,}\d)"

    if re.search(email_pattern, resume_text):
        score += 5
    else:
        suggestions.append("Add a professional email address.")

    if re.search(phone_pattern, resume_text):
        score += 5
    else:
        suggestions.append("Add your phone number.")

    # ------------------------
    # Skills
    # ------------------------

    if len(skills) >= 10:
        score += 20

    elif len(skills) >= 6:
        score += 15

    elif len(skills) >= 3:
        score += 10

    else:
        score += 5
        suggestions.append("Add more technical skills.")

    # ------------------------
    # GitHub
    # ------------------------

    if github != "Not Found":
        score += 5
    else:
        suggestions.append("Add your GitHub profile.")

    # ------------------------
    # LinkedIn
    # ------------------------

    if linkedin != "Not Found":
        score += 5
    else:
        suggestions.append("Add your LinkedIn profile.")

    # ------------------------
    # Projects
    # ------------------------

    if "project" in resume_text.lower():
        score += 15
    else:
        suggestions.append("Mention your academic or personal projects.")

    # ------------------------
    # Education
    # ------------------------

    education_keywords = [
        "b.tech",
        "bachelor",
        "university",
        "college",
        "cgpa",
        "degree"
    ]

    if any(word in resume_text.lower() for word in education_keywords):
        score += 10
    else:
        suggestions.append("Include your education details.")

    # ------------------------
    # Experience
    # ------------------------

    experience_keywords = [
        "intern",
        "experience",
        "worked",
        "company"
    ]

    if any(word in resume_text.lower() for word in experience_keywords):
        score += 20
    else:
        suggestions.append("Add internships or work experience.")

    # ------------------------
    # Certifications
    # ------------------------

    cert_keywords = [
        "certificate",
        "certification",
        "certified"
    ]

    if any(word in resume_text.lower() for word in cert_keywords):
        score += 10
    else:
        suggestions.append("Mention your certifications.")

    # ------------------------
    # Resume Length
    # ------------------------

    word_count = len(resume_text.split())

    if word_count >= 250:
        score += 5
    else:
        suggestions.append("Expand your resume with more details.")

    return score, suggestions