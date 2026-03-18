from dotenv import load_dotenv
import os

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
#from openai import OpenAI   # disabled

load_dotenv()

#client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))  # disabled

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

db = FAISS.load_local(
    "vector_db",
    embeddings
)

def generate_report(tamper_result, ocr_text):

    docs = db.similarity_search(ocr_text)

    context = "\n".join([d.page_content for d in docs])

    prompt = f"""
You are an AI fraud detection assistant.

Knowledge:
{context}

Image Analysis:
{tamper_result}

Extracted Text:
{ocr_text}

Generate a structured fraud risk report.
"""

    # ---- OpenAI call disabled ----
    """
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a fraud detection assistant."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content
    """

    # Return a simple report instead
    report = f"""
Fraud Detection Report

Tamper Check:
{tamper_result}



Relevant Knowledge:
{context}

Risk Assessment:
Manual review recommended.
"""

    return report