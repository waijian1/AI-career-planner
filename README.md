🚀 AI Career Planner

An AI-powered tool that helps you analyze real job market demands in your country and generate a personalized study plan for your target career.

This project uses live job data + AI to guide what you should learn — instead of guessing.

📌 Overview

Many learners struggle with:

❓ What skills to learn

❓ Whether those skills are actually in demand

❓ How to structure a learning roadmap

This project solves that by:

Extracting real job data from the market (Your Country)

Identifying in-demand skills

(Planned) Generating a custom AI-driven study plan

✨ Features
🔍 Job Search API Integration

Uses JSearch (RapidAPI) to fetch real job listings

Filters:

📍 Country: Can be change based on your preference

📅 Posted within last week (can be change based on your preference)

Extracts:

Job title

Company name

Job description

📊 Structured Job Data Extraction

Converts raw API response into clean Python objects:

{
    "title": "Machine Learning Engineer",
    "company": "Company Name",
    "description": "Job description text..."
}
🧠 (Planned) AI Career Intelligence

Analyze job descriptions to extract:

Skills (Python, SQL, ML, etc.)

Tools (Docker, AWS, etc.)

Identify:

Most demanded skills

Skill gaps

📚 (Planned) Study Plan Generator

Generate:

Step-by-step roadmap

Learning priorities

Project suggestions

🏗️ Tech Stack

Python

Requests (API calls)

RapidAPI (JSearch)

dotenv (environment management)

⚙️ How It Works

User specifies a job query
Example:

machine learning engineer in singapore

System calls JSearch API

Extracts key job information:

Title

Company

Description

Returns structured job dataset for further analysis

📂 Project Structure
AI-career-planner/
│
├── jobsearchapi.py     # Fetches job data from RapidAPI (JSearch)
├── main.ipynb          # Experimentation / analysis notebook
├── .env                # API keys (not committed)
└── README.md

🚀 Getting Started
1. Clone the repo
git clone https://github.com/waijian1/AI-career-planner.git
cd AI-career-planner
2. Install dependencies
uv sync
3. Set up API key

Create a .env file:

X_RAPID_API_KEY=your_rapidapi_key
GOOGLE_API_KEY=your_google_api_key
4. Test the script
uv run jobsearchapi.py
5. Run LLM to generate career plan
main.ipynb

📊 Example Usage
from jobsearchapi import search_job

jobs = search_job("machine learning engineer in singapore")

print(jobs[:2])
📈 Example Output
[
  {
    "title": "Machine Learning Engineer",
    "company": "ABC Company",
    "description": "We are looking for..."
  },
  ...
]

🔮 Roadmap (Next Steps)

 Extract skills using NLP / LLM

 Aggregate most in-demand skills

 Generate personalized study plans

 Build Streamlit UI

 Deploy as a web app


📜 License

MIT License

👨‍💻 Author

Lim Wai Jian
GitHub: https://github.com/waijian1

⭐ Support

If you find this useful:

Star ⭐ the repo

Share it with others

Contribute improvements 🚀