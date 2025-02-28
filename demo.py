import streamlit as st
import random
import pandas as pd
from fpdf import FPDF

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

# Section 2: Resume Generator
st.header("📄 Resume Generator")

def generate_resume():
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    
    # Title
    pdf.cell(200, 10, f"{name}'s Resume", ln=True, align='C')
    pdf.ln(10)

    # Contact Information
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, f"📧 {email} | 📞 {phone} | 🌐 {linkedin} | 💻 {github}", ln=True, align='C')
    pdf.ln(10)

    # Education
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "Education", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 8, f"{education} at {university} | CGPA: {cgpa}")
    pdf.ln(5)

    # Experience
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "Experience", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 8, f"{experience} years of experience in {career_goal}")
    pdf.ln(5)

    # Skills
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "Technical Skills", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 8, skills)
    pdf.ln(5)

    # Certifications
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "Certifications", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 8, certifications)
    pdf.ln(5)

    # Extracurriculars
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "Extracurricular Activities", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 8, extracurriculars)
    pdf.ln(5)

    # Save as PDF
    pdf_output = "resume.pdf"
    pdf.output(pdf_output)
    return pdf_output

if st.button("Generate Resume"):
    resume_file = generate_resume()
    st.success("✅ Resume Generated Successfully!")
    with open(resume_file, "rb") as file:
        st.download_button(label="📥 Download Resume", data=file, file_name="My_Resume.pdf", mime="application/pdf")

# Section 3: Mock Interview Simulator
st.header("🎤 Mock Interview Simulator")
questions = [
    "Tell me about yourself.",
    "What are your strengths and weaknesses?",
    "Where do you see yourself in 5 years?",
    "Why should we hire you?",
    "Describe a challenging project you worked on.",
    "How do you handle feedback and criticism?",
    "What motivates you at work?",
    "How do you prioritize tasks when handling multiple projects?"
]
if st.button("Start Interview"):
    st.write(f"**Question:** {random.choice(questions)}")

# Section 4: Job Market Analysis Dashboard
st.header("📊 Job Market Analysis Dashboard")
st.write("🔍 Fetching job market trends...")

st.write("🚀 Thank you for using the AI Career Counselor!")
