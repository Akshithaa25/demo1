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
education = st.selectbox("Highest Education Level:", ["High School", "Bachelor's", "Master's", "PhD"])
experience = st.slider("Years of Work Experience:", 0, 30, 0)
skills = st.text_area("List your skills (comma separated):")
career_goal = st.text_input("Your Dream Job:")

if st.button("Save Profile"):
    st.success(f"Profile saved for {name}! 🚀")

# Section 2: Resume & Cover Letter Generator
st.header("📄 Resume & Cover Letter Generator")
resume_template = f"""
**Name:** {name}
**Education:** {education}
**Experience:** {experience} years
**Skills:** {skills}
**Career Goal:** {career_goal}
"""
if st.button("Generate Resume"):
    st.text_area("Your AI-Generated Resume:", resume_template, height=150)

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
