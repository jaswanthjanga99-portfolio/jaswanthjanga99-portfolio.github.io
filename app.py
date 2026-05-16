from flask import Flask, render_template

app = Flask(__name__)

projects = [
    {
        "title": "AI Resume Analyzer (NLP)",
        "tech": "Python, Flask, NLP, Transformers",
        "bullets": [
            "Parsed resumes into structured skills/entities using NLP-based extraction.",
            "Matched resume↔JD using embedding similarity + normalization for better calibration.",
            "Produced actionable scores and skill gaps with clear, explainable outputs.",
        ],
        "highlights": "Outcome: resume-vs-job similarity scoring and skill-gap summaries designed for recruiter review."
    },
    {
        "title": "LLM-Powered Chat Assistant",
        "tech": "Python, LLMs, Retrieval, Prompting",
        "bullets": [
            "Implemented RAG-style retrieval over documents to ground answers.",
            "Added conversation context/memory to improve coherence across turns.",
            "Built safety-focused prompting to reduce hallucinations and unsafe responses.",
        ],
        "highlights": "Outcome: document Q&A assistant with grounded responses and better conversation continuity."
    },
    {
        "title": "Image Classifier (Computer Vision)",
        "tech": "Python, PyTorch/TensorFlow, OpenCV",
        "bullets": [
            "Trained CNN classifier with evaluation (accuracy/F1) and error analysis.",
            "Created an inference-ready pipeline (preprocessing + postprocessing) for API serving.",
            "Optimized for real-world usage with robust input handling and deployment workflow.",
        ],
        "highlights": "Outcome: a production-style model pipeline—training → evaluation → inference."
    }
]

skills = [
    "NLP (Transformers, embeddings, extraction)",
    "LLM Apps (RAG, prompting, evaluation)",
    "Computer Vision (CNNs, OpenCV pipelines)",
    "Python, Flask, REST APIs",
    "Data Preprocessing & Experimentation"
]

highlights = [
    {"title": "Impact-driven", "desc": "I design projects around measurable evaluation and iterative improvement."},
    {"title": "Explainable outputs", "desc": "Focus on clear summaries (skill gaps, grounded answers) over black-box results."},
    {"title": "Practical engineering", "desc": "Pipelines that go from training/inference to usable apps/APIs."}
]


@app.route('/')
def home():
    return render_template('index.html', projects=projects, skills=skills, highlights=highlights)


if __name__ == '__main__':
    app.run(debug=True)

