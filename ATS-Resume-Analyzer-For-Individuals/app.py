from flask import Flask, request, render_template, jsonify
import PyPDF2
import os

app = Flask(__name__)

# Sample keywords (you can replace with job-specific ones)
JOB_KEYWORDS = [
    'python', 'java', 'c++', 'javascript', 'html', 'css', 'sql', 'mysql', 'postgresql',
    'mongodb', 'nosql', 'machine learning', 'deep learning', 'data analysis', 'data visualization',
    'power bi', 'tableau', 'excel', 'data science', 'ai', 'nlp', 'computer vision',
    'git', 'github', 'bitbucket', 'rest api', 'graphql', 'json', 'xml',
    'docker', 'kubernetes', 'linux', 'bash', 'agile', 'scrum', 'jira', 'ci/cd',
    'unit testing', 'integration testing', 'problem solving', 'communication',
    'teamwork', 'time management', 'cloud', 'aws', 'azure', 'gcp', 'lambda',
    'serverless', 'data engineering', 'etl', 'big data', 'hadoop', 'spark'
]

def extract_text_from_pdf(file_path):
    text = ''
    with open(file_path, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            text += page.extract_text() or ''
    return text.lower()

def calculate_ats_score(resume_text, keywords):
    matches = [kw for kw in keywords if kw.lower() in resume_text]
    score = len(matches) / len(keywords) * 100  # Score out of 100
    return round(score, 2), matches

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_resume():
    if 'resume' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    
    file = request.files['resume']
    filepath = os.path.join('uploads', file.filename)
    file.save(filepath)

    resume_text = extract_text_from_pdf(filepath)
    score, matched_keywords = calculate_ats_score(resume_text, JOB_KEYWORDS)

    os.remove(filepath)  # Clean up

    return jsonify({
        'ats_score': score,
        'matched_keywords': matched_keywords,
        'total_keywords': JOB_KEYWORDS
    })

if __name__ == '__main__':
    os.makedirs('uploads', exist_ok=True)
    app.run(debug=True)
