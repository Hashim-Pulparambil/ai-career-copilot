import json
import re


def load_skills():
    with open("data/skills.json", "r") as file:
        return json.load(file)


def extract_email(text):
    match = re.search(
        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
        text
    )
    return match.group() if match else "Not Found"


def extract_phone(text):
    match = re.search(
        r"(\+?\d[\d\s-]{8,}\d)",
        text
    )
    return match.group() if match else "Not Found"


def extract_github(text):
    match = re.search(
        r"github\.com/[A-Za-z0-9_-]+",
        text,
        re.IGNORECASE,
    )
    return match.group() if match else "Not Found"


def extract_linkedin(text):
    match = re.search(
        r"linkedin\.com/in/[A-Za-z0-9_-]+",
        text,
        re.IGNORECASE,
    )
    return match.group() if match else "Not Found"


def extract_skills(text):
    skills_db = load_skills()

    found = []

    lower_text = text.lower()

    for category in skills_db.values():
        for skill in category:
            if skill.lower() in lower_text:
                found.append(skill)

    return sorted(list(set(found)))