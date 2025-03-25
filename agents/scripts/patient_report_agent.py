from crewai import Agent, Task, Crew
import yagmail
import json
import chromadb
from sentence_transformers import SentenceTransformer
from chromadb.config import Settings

import chromadb
from chromadb.config import Settings



# === CONFIG ===
CARETAKER_ID = "C023"
CARETAKER_EMAIL = "jabinbalanr@gmail.com"
patient_id = "David Johnson"

# === Agent 1: Retrieve Patient Info ===
def retrieve_patients_for_caretaker(caretaker_id, patient_id):
    chroma_client = chromadb.PersistentClient(
    path="/workspace/vectorDB/healthcare_db"
    )

    collection = chroma_client.get_collection("healthcare")
    embedder = SentenceTransformer("all-MiniLM-L6-v2")

    query = f"Patients name: {patient_id}"
    query_embedding = embedder.encode([query])[0].tolist()
    results = collection.query(query_embeddings=[query_embedding], n_results=10)
    matched_docs = results["documents"][0]
    print(matched_docs)

    filtered_docs = [doc for doc in matched_docs if patient_id in doc]
    return filtered_docs


# === Agent 2: Format to Table ===
def format_patient_info_as_table(patient_strings):
    table = "<table border='1'><tr><th>Name</th><th>Issue</th><th>Age</th><th>Allergies</th></tr>"
    for entry in patient_strings:
        name = "Unknown"
        age = "-"
        issue = "-"
        allergy = "-"
        try:
            parts = entry.split("Patient ")[1].split(" is ")
            name = parts[0]
            rest = parts[1].split(" years old from ")[0]
            age = rest
            issue = entry.split("suffering from ")[1].split(".")[0]
            allergy = entry.split("Allergies: ")[1].split(".")[0]
        except:
            pass
        table += f"<tr><td>{name}</td><td>{issue}</td><td>{age}</td><td>{allergy}</td></tr>"
    table += "</table>"
    return table

# === Agent 3: Send Email ===
def send_email_to_caretaker(to_email, subject, html_body):
    yag = yagmail.SMTP(user="16p114@gmail.com", password="xxxxxx")
    yag.send(to=to_email, subject=subject, contents=html_body)

# === Crew Execution ===
patient_data = retrieve_patients_for_caretaker(CARETAKER_ID, patient_id)
html_report = format_patient_info_as_table(patient_data)
send_email_to_caretaker(CARETAKER_EMAIL, "Patient Report for Today", html_report)

print("Email sent to caretaker with patient info!")
print(html_report)
