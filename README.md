#  Smart Resume Analyzer
   Live Link - https://resume-pro-analyzer.streamlit.app/

A powerful AI-driven resume analysis tool built using **Google Gemini LLM** and **Streamlit**. It compares a candidate's resume with a given job description and provides intelligent suggestions, missing keywords, skill improvements, and match percentage — helping candidates tailor their resumes more effectively for job roles.

---

##  Features

-  Upload your resume in **PDF** format
-  Paste a **Job Description**
-  Get a summary of your resume in simple language
-  Get **skill improvement** suggestions based on JD
-  Discover **keywords missing** in your resume
-  Get a **match score (%)** with explanation
-  Ask **custom questions** about your resume
-  Powered by **Gemini 2.5 Flash LLM**

---

##  Tech Stack

| Component      | Technology                     |
|----------------|--------------------------------|
| Frontend       | Streamlit                      |
| AI Model       | Google Gemini 2.5 Flash (LLM)  |
| Resume Parsing | pdfplumber                     |
| Secrets        | python-dotenv + .env file      |
| Language       | Python                         |

---

##  Project Structure

smart-resume-analyzer/
│
├── app.py # Main Streamlit app
├── .env # Contains Gemini API Key (not uploaded)
├── requirements.txt # All required Python packages
├── README.md # This documentation
└── .gitignore # To ignore .env, pycache, etc.




---

##  How to Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/smart-resume-analyzer.git
cd smart-resume-analyzer


2. Install dependencies

pip install -r requirements.txt


3. Add your Gemini API key
Create a .env file in the project root and add:

GOOGLE_API_KEY=your_gemini_api_key_here


4. Run the Streamlit app

streamlit run app.py



Example Use Case

Job Description: Data Scientist with experience in ML, Python, and NLP

Resume: Uploaded PDF containing your experience and skills

Output:
- Summary of resume
- Missing keywords like "NLP", "TensorFlow"
- Suggestions: Add certifications in ML, mention specific projects
- Match Score: 72%



 Use Cases 

- Candidates tailoring their resume for a specific job
- HR teams screening resumes more effectively
- Career coaches preparing mock interviews
- Students preparing for placements


Future Improvements

- Support `.docx` resume format
- Generate PDF report of analysis
- Upload multiple resumes (batch analysis)
- Add role-specific question generation (e.g., Data Scientist, Backend Dev)
- Deploy app on Hugging Face / Render


Deployment Link 
 https://resume-pro-analyzer.streamlit.app/

 Author
Suraj Kumar
Final Year | B.Tech CSE (AI & ML)

 License
This project is for educational/demo purposes only.
LLM usage must comply with Gemini API Terms of Use.
