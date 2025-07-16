# This file is used for extracting more information like experience, skills, tools from the description
# extracted before and convert all into a single csv file known as enriched_job.csv
# Here with the help of LLM I am able to extract further information into a file
import os
import json
import pandas as pd
from langchain_groq import ChatGroq
from langchain.schema import SystemMessage, HumanMessage
from dotenv import load_dotenv

# Groq API key
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

# ChatGroq LLM
llm = ChatGroq(
    api_key=groq_api_key,
    model_name="llama3-70b-8192"
)

def extract_structured_info(description):
    prompt = f"""
Extract the following information from the job description:
- Total experience (in years or range)
- Skills (conceptual or programming)
- Tools (databases, BI tools, orchestration platforms)

Return ONLY valid JSON in this format:
{{
  "experience": "...",
  "skills": ["...", "..."],
  "tools": ["...", "..."]
}}

Job Description:
\"\"\"{description}\"\"\"
"""

    response = llm.invoke([
        SystemMessage(content="You are a helpful assistant that extracts structured job info."),
        HumanMessage(content=prompt)
    ])

    try:
        return json.loads(response.content)
    except json.JSONDecodeError:
        print("⚠️ JSON parsing failed. Output was:\n", response.content)
        return {"experience": "", "skills": [], "tools": []}


def parse_and_save():
    with open("raw_jobs.json", "r", encoding="utf-8") as f:
        jobs = json.load(f)

    enriched_jobs = []
    for job in jobs:
        try:
            extracted = extract_structured_info(job["description"])
            job.update({
                "experience": extracted.get("experience", ""),
                "skills": ", ".join(extracted.get("skills", [])),
                "tools": ", ".join(extracted.get("tools", []))
            })
            enriched_jobs.append(job)
        except Exception as error:
            print(f"Failed to extract for job: {job.get('title')} – {error}")

    df = pd.DataFrame(enriched_jobs)
    df.to_csv("enriched_jobs.csv", index=False)
    print("Enriched job data saved to enriched_jobs.csv")

if __name__ == "__main__":
    parse_and_save()