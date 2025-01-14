<h1>ATS Resume Expert</h1>
<br>
ATS Resume Expert is a web-based application designed to evaluate resumes against job descriptions using a combination of advanced AI models and applicant tracking system (ATS) functionalities. This tool helps candidates align their resumes with job requirements for data science, full-stack development, big data engineering, DevOps, and related technical fields.
<br>
<h3>Features</h3>
<ul>
<li>Resume Evaluation: Provides detailed feedback on how well a resume aligns with a job description.</li>
<li>ATS Scanning: Simulates ATS functionality to identify keyword matches and suggests improvements.</li>
<li>Percentage Match: Outputs a percentage match score along with missing keywords and overall evaluation.</li>
</ul>
Tech Stack
Frontend: Streamlit
Backend: Python
AI Integration: Google Generative AI (Gemini 1.5 Flash)
PDF Processing: pdf2image, Pillow
Environment Configuration: dotenv
Installation
Clone the repository:
bash
Copy code
git clone https://github.com/your-username/ats-resume-expert.git
cd ats-resume-expert
Install the required Python packages:
bash
Copy code
pip install -r requirements.txt
Set up your environment variables:
Create a .env file in the project directory.
Add your Google Generative AI API key:
makefile
Copy code
GOOGLE_API_KEY=your_api_key
Usage
Run the application:
bash
Copy code
streamlit run app.py
Open the app in your browser at http://localhost:8501.
Enter the job description in the text area.
Upload a PDF of your resume.
Choose one of the available actions:
Tell me about the Resume: Receive a professional evaluation of your resume.
Percentage Match: Get a match score and recommendations for improvement.
Project Structure
bash
Copy code
├── app.py             # Main application code
├── requirements.txt   # List of dependencies
├── .env               # Environment variables (not included in the repo)
└── README.md          # Project documentation
Future Enhancements
Support for multiple resume formats (e.g., DOCX).
Integration with additional job boards and ATS systems.
Enhanced AI models for more nuanced resume evaluation.
License
This project is licensed under the MIT License. See the LICENSE file for details.

Would you like to customize this further?
