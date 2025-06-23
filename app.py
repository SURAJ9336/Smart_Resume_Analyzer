import streamlit as st
import pypdf
import os
from dotenv import load_dotenv
import google.generativeai as genai

# Loading  Gemini API key from .env file
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


# title and page settings
st.set_page_config(page_title="Smart Resume Analyzer", layout="centered")
st.title(" Smart Resume Analyzer")
st.write("This Application helps you in your Resume Review with help of **GEMINI AI (LLM)**")

#Job Description input
job_description = st.text_area("Job Description:", height=150)

# Upload resume
uploaded_resume = st.file_uploader("Upload your Resume (PDF)...", type=["pdf"])

#Extract text from uploaded resume
def extract_text_from_pdf(file):
    reader = pypdf.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text

#  Function to send prompt to Gemini
def ask_gemini(prompt):
    model = genai.GenerativeModel('gemini-2.5-flash')
    response = model.generate_content(prompt)
    return response.text

# Process the resume if uploaded
resume_text = ""
if uploaded_resume is not None:
    resume_text = extract_text_from_pdf(uploaded_resume)

# Add feature buttons
if st.button("Tell Me About the Resume") and resume_text:
    st.info("Analyzing your resume...")
    prompt = f"Read this resume:\n{resume_text}\n\nTell me what this resume is about in simple language."
    response = ask_gemini(prompt)
    st.success(response)

if st.button("How Can I Improvise my Skills") and resume_text and job_description:
    st.info("Checking for skill improvement...")
    prompt = f"Based on the job description below, suggest how this person can improve their skills.\n\nJob Description:\n{job_description}\n\nResume:\n{resume_text}"
    response = ask_gemini(prompt)
    st.success(response)

if st.button("What are the Keywords That are Missing") and resume_text and job_description:
    st.info("Finding missing keywords...")
    prompt = f"Compare the following resume and job description. List keywords missing from the resume that are important in the job description.\n\nJob Description:\n{job_description}\n\nResume:\n{resume_text}"
    response = ask_gemini(prompt)
    st.success(response)

if st.button("Percentage match") and resume_text and job_description:
    st.info("Calculating resume match score...")
    prompt = f"Rate how well this resume matches the job description on a scale of 1 to 100 and explain the reason.\n\nJob Description:\n{job_description}\n\nResume:\n{resume_text}"
    response = ask_gemini(prompt)
    st.success(response)

# Custom question box
custom_question = st.text_input("Any Questions?")
if st.button("Go") and custom_question and resume_text:
    st.info("Asking your custom question...")
    prompt = f"This is the resume:\n{resume_text}\n\nAnswer this question:\n{custom_question}"
    response = ask_gemini(prompt)
    st.success(response)
