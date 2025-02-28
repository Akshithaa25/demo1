from fpdf import FPDF
import streamlit as st
import random
import pandas as pd
import requests

st.set_page_config(page_title="AI Career Counselor", page_icon="🎯")

# Title
st.title("🎯 AI-Powered Virtual Career Counselor")

# Section 1: User Profile Management
st.header("👤 User Profile")
name = st.text_input("Enter your Name:")
email = st.text_input("Enter your Email:")
phone = st.text_input("Enter your Phone Number:")
linkedin = st.text_input("LinkedIn Profile URL:")
github = st.text_input("GitHub Profile URL:")
education = st.selectbox("Highest Education Level:", ["High School", "Bachelor's", "Master's", "PhD"])
university = st.text_input("University Name:")
cgpa = st.text_input("Your CGPA (Optional):")
experience = st.slider("Years of Work Experience:", 0, 30, 0)
skills = st.text_area("List your skills (comma separated):")
career_goal = st.text_input("Your Dream Job:")
certifications = st.text_area("List Certifications (comma separated):")
extracurriculars = st.text_area("List Extracurricular Activities (comma separated):")

if st.button("Save Profile"):
    st.success(f"Profile saved for {name}! 🚀")

# Section 2: Resume & Cover Letter Generator

def generate_resume(name, email, phone, linkedin, github, education, university, cgpa, experience, skills, certifications, extracurriculars, career_goal):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    
    # Title
    pdf.set_font("Arial", "B", 16)
    pdf.cell(200, 10, f"{name}'s Resume", ln=True, align='C')
    pdf.ln(10)

    # Contact Information
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 8, f"📧 {email}  |  📞 {phone}  |  🌐 {linkedin}  |  💻 {github}", align="C")
    pdf.ln(8)

    # Education
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "🎓 Education", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 8, f"{education} at {university} (CGPA: {cgpa})")
    pdf.ln(5)

    # Experience
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "💼 Experience", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 8, f"{experience} years of experience in {career_goal}")
    pdf.ln(5)

    # Skills
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "🛠️ Skills", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 8, skills)
    pdf.ln(5)

    # Certifications
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "📜 Certifications", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 8, certifications)
    pdf.ln(5)

    # Extracurriculars
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "🎭 Extracurricular Activities", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 8, extracurriculars)
    pdf.ln(5)

    # Career Goal
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "🎯 Career Goal", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 8, career_goal)
    pdf.ln(5)

    # Save PDF
    pdf_output = "resume.pdf"
    pdf.output(pdf_output)
    return pdf_output

st.header("📄 Resume Generator")

if st.button("Generate Resume"):
    resume_file = generate_resume(name, email, phone, linkedin, github, education, university, cgpa, experience, skills, certifications, extracurriculars, career_goal)
    st.success("✅ Resume Generated Successfully!")
    with open(resume_file, "rb") as file:
        st.download_button(label="📥 Download Resume", data=file, file_name="My_Resume.pdf", mime="application/pdf")
# Section 3: Skill Enhancement & Course Recommendations
st.header("📚 Skill Enhancement & Course Recommendations")
if skills:
    st.write("🔍 Searching for courses based on your skills...")
    # Simulated Course Recommendations
    recommended_courses = ["Python for Data Science", "Machine Learning Basics", "Project Management"]
    for course in recommended_courses:
        st.markdown(f"- 📌 {course}")

# Section 4: Mock Interview Simulator
st.header("🎤 Mock Interview Simulator")
questions = [
    "Tell me about yourself.",
    "What are your strengths and weaknesses?",
    "Where do you see yourself in 5 years?",
    "Why should we hire you?",
    "Describe a challenging project you worked on."
]
if st.button("Start Interview"):
    st.write(f"**Question:** {random.choice(questions)}")

# Section 5: Job Market Analysis Dashboard
st.header("📊 Job Market Analysis Dashboard")
st.write("🔍 Fetching job market trends...")

# Fetch real-time job data (Example API - Adzuna)
API_ID = "0e94face"  # Replace with your Adzuna API ID
API_KEY = "6dac6d7f2817df907ee89743a31dd58c"  # Replace with your Adzuna API Key
JOB_API_URL = f"https://api.adzuna.com/v1/api/jobs/us/search/1?app_id={API_ID}&app_key={API_KEY}&results_per_page=5"

if st.button("Show Job Trends"):
    response = requests.get(JOB_API_URL)
    if response.status_code == 200:
        jobs = response.json()["results"]
        for job in jobs:
            st.write(f"📌 **{job['title']}** - {job['company']['display_name']}")
            st.write(f"📍 Location: {job['location']['display_name']}")
            st.write(f"💰 Salary Estimate: {job.get('salary_min', 'N/A')} - {job.get('salary_max', 'N/A')}")
            st.write(f"🔗 [Job Link]({job['redirect_url']})")
            st.write("---")
    else:
        st.error("⚠ Could not fetch job data. Please check your API credentials.")

st.write("🚀 Thank you for using the AI Career Counselor!")
