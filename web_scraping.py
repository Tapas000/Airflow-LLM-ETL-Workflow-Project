# This file is used for extracting job data using SerpApi and extract job title, location, company and description
# Then it save it in json format for further information extraction
import os
from serpapi import GoogleSearch
import json
from dotenv import load_dotenv
load_dotenv()

SERPAPI_Api_key = os.getenv("SERPAPI_KEY")

def scrape_jobs(api_key, query="data engineer", location="India", num_jobs=10):
    params = {
        "engine": "google_jobs",
        "q": query,
        "location": location,
        "hl": "en",
        "api_key": api_key
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    jobs = results.get("jobs_results", [])[:num_jobs]

    job_list = []
    for job in jobs:
        job_data = {
            "title": job.get("title"),
            "company": job.get("company_name"),
            "location": job.get("location"),
            "description": job.get("description", "")
        }
        job_list.append(job_data)

    with open("raw_jobs.json", "w", encoding="utf-8") as f:
        json.dump(job_list, f, indent=2)

    print(f"Saved {len(job_list)} jobs to raw_jobs.json")

if __name__ == "__main__":
    SERPAPI_KEY = os.getenv("SERPAPI_API_KEY")
    scrape_jobs(SERPAPI_KEY)

