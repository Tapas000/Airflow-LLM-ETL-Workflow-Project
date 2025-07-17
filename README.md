# 🛠️ Job Data ETL Pipeline with Airflow & LLM Enrichment

This project demonstrates an end-to-end ETL pipeline to extract, enrich, and store job listings using **Apache Airflow**, **SerpAPI**, **Large Language Models (LLMs)**, and **PostgreSQL**.

---
<img width="1072" height="552" alt="image" src="https://github.com/user-attachments/assets/97877084-c7d4-4756-95f2-49532e40dd78" />
## 🚀 Overview

This pipeline:
1. Uses **SerpAPI** to fetch raw job listings from Google Jobs.
2. Extracts key fields like **title**, **company**, **location**, and **description**.
3. Applies **LLM-based enrichment** to extract **experience**, **skills**, and **tools** from unstructured job descriptions.
4. Combines all information into a final CSV (`enriched_jobs.csv`).
5. Loads the structured data into a **PostgreSQL** table.

All tasks are orchestrated using **Apache Airflow**.

---

## 🛠️ Tools & Technologies

| Layer            | Tool/Tech                         |
|------------------|-----------------------------------|
| Orchestration     | Apache Airflow (2.9.1)             |
| Data Extraction   | SerpAPI (Google Job Results)       |
| NLP Enrichment    | Grok API / Langchain               |
| Transformation    | Python, Pandas                     |
| Database          | PostgreSQL                         |
| Containerization  | Docker, Docker Compose             |

---



---

## 🔄 Airflow Workflow (`llm_job_etl_pipeline`)

1. **extract_jobs_from_serpapi**  
   Uses SerpAPI to fetch job data and save to `raw_jobs.json`.

2. **llm_enrich_job_descriptions**  
   Uses an LLM to extract structured fields like required experience, tools, and skills from descriptions.

3. **load_to_postgres**  
   Loads `enriched_jobs.csv` into a PostgreSQL database table.

---

## 🧪 Sample Enriched Output

| Title        | Company | Location  | Skills               | Experience | Tools           |
| ------------ | ------- | --------- | -------------------- | ---------- | --------------- |
| Data Analyst | Google  | Bangalore | SQL, Python, Tableau | 2–4 years  | Excel, BigQuery |


---



