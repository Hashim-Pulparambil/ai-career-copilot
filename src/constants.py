"""
Application constants used by CareerPilot AI.
"""

# ATS Section Weights
SECTION_WEIGHTS = {
    "Contact Information": 10,
    "Education": 15,
    "Skills": 20,
    "Projects": 15,
    "Experience": 20,
    "Certifications": 10,
    "Resume Length": 5,
    "Online Profiles": 5,
}

# Resume Grades
GRADE_SCALE = [
    (90, "A+"),
    (80, "A"),
    (70, "B"),
    (60, "C"),
    (0, "D"),
]

# Education Keywords
EDUCATION_KEYWORDS = [
    "b.tech",
    "bachelor",
    "master",
    "m.tech",
    "degree",
    "college",
    "university",
    "cgpa",
]

# Experience Keywords
EXPERIENCE_KEYWORDS = [
    "intern",
    "internship",
    "experience",
    "worked",
    "company",
    "developer",
    "engineer",
]

# Certification Keywords
CERTIFICATION_KEYWORDS = [
    "certificate",
    "certification",
    "certified",
    "coursera",
    "udemy",
    "nptel",
    "google",
    "microsoft",
    "aws",
]

# Project Keywords
PROJECT_KEYWORDS = [
    "project",
    "developed",
    "built",
    "implemented",
    "github",
]

# Suggestions
DEFAULT_SUGGESTIONS = {
    "experience": "Add internship, freelance or work experience.",
    "certification": "Add certifications relevant to your career goal.",
    "projects": "Include at least 2–3 academic or personal projects.",
    "skills": "Add more technical skills relevant to your target role.",
    "github": "Include your GitHub profile.",
    "linkedin": "Include your LinkedIn profile.",
    "education": "Add complete education details.",
    "length": "Expand your resume to at least 250 words.",
}