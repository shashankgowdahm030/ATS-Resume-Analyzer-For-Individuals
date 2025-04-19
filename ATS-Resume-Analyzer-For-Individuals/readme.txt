# Resume ATS Scorer with Flask

This Flask-based web application allows users to upload a resume (in PDF format), which is then processed to extract the text and calculate an Applicant Tracking System (ATS) score based on predefined job-specific keywords. The app also returns a list of matched keywords from the resume.

### 🧑‍💻 Developed By
Shashank Gowda H M  
📸 Instagram: [shashank.gowda.hm]

---

## 🚀 Features

- Upload a resume (PDF format) for analysis.
- Extracts text from the uploaded PDF.
- Calculates an ATS score based on how well the resume matches a list of job-specific keywords.
- Returns a JSON response containing:
  - The ATS score (out of 100).
  - A list of matched keywords from the resume.
  - A list of all predefined job keywords.

---

## 📁 Project Structure

project/ ├── uploads/ # Uploaded resumes temporarily stored here ├── templates/ │ └── index.html # HTML page for uploading resumes ├── app.py # Main Flask app to handle backend logic ├── requirements.txt # Python dependencies └── README.md # Project documentation

yaml
Copy
Edit

---

## 📦 Requirements

Create a virtual environment and install the required dependencies:

```bash
pip install -r requirements.txt
Or, install them manually:

bash
Copy
Edit
pip install Flask==2.2.5
pip install PyPDF2==1.26.0
▶️ How to Run
Clone the repository and navigate to the project folder:

bash
Copy
Edit
git clone <repository-url>
cd <project-folder>
Run the Flask app:

bash
Copy
Edit
python app.py
Open your browser and go to:

http://127.0.0.1:5000/

📝 How It Works
Resume Upload: You can upload a PDF resume on the web interface.

Text Extraction: The app extracts text from the uploaded PDF using the PyPDF2 library.

ATS Scoring: The app calculates a score based on how many of the predefined keywords are present in the resume text.

JSON Response: After processing, the app returns the score and matched keywords in JSON format.

🎯 ATS Scoring Method
The ATS score is calculated as the percentage of predefined keywords found in the resume text.

The formula used to calculate the score is:

mathematica
Copy
Edit
ATS Score = (Number of Matches / Total Keywords) * 100
🖼 Example
Upload a Resume:

Choose a PDF file and click the "Upload" button.

Processing:

The app will extract text from the resume and compare it with a list of predefined job-related keywords.

Results:

The app will return a JSON response with:

ats_score: A score representing how well the resume matches the job keywords.

matched_keywords: A list of keywords found in the resume.

total_keywords: A complete list of predefined keywords used for matching.

📜 License
Free to use and modify. If you use this code, a star ⭐ on GitHub is appreciated!

📄 requirements.txt
ini
Copy
Edit
Flask==2.2.5
PyPDF2==1.26.0