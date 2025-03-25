#  LLM-Powered Healthcare Assistant

An end-to-end AI-driven assistant designed for caretakers and healthcare professionals. This intelligent system allows users to query patient data, retrieve policy and departmental contact information, and receive structured responses and automated email updates. The assistant is built using a fine-tuned LLaMA 2 model, ChromaDB for vector search, and CrewAI for agent-driven workflows, all accessible via a clean Streamlit frontend.

---

##  Objective

To minimize human error and improve patient care coordination by creating an automated system that answers natural language questions with accurate healthcare data, delivering reports directly to caretakers through email.

---

##  Key Features

- **Natural Language Q&A** on patients, departments, policies, and contacts.
- **Fine-tuned LLaMA 2** (`meta-llama/Llama-2-7b-hf `) on structured healthcare metadata using PEFT (LoRA).
- **ChromaDB** + `sentence-transformers` for efficient **RAG (Retrieval-Augmented Generation)**.
- **CrewAI Agents** to retrieve patient info, format data into HTML, and send emails.
- **Streamlit UI** for seamless natural language interaction.
- **Automated Email Reports** to caretakers (with allergy info, contacts, age, etc.).
- **Modular and Scalable Architecture** suitable for integration with real-world EHR systems.

---

## Project Workflow
![image](https://github.com/user-attachments/assets/1bd21a7a-2e92-4a67-911c-fd9466cddfb7)


##  Project Structure

```
/workspace/
├── agents/
│   └── scripts/
│       └── patient_report_agent.py     # CrewAI agent: retrieval → HTML → email
│
├── vectorDB/
│   ├── script/
│   │   ├── healthcare_docs.json        # Domain-specific metadata (policies, allergies, contacts)
│   │   └── index_to_chroma.py          # Embeds & indexes data in ChromaDB
│   └── healthcare_db/                  # Chroma vector store
│
├── app/
│   └── app.py                          # Streamlit frontend w/ RAG + model integration
│
├── output/
│   └── trained_llama2/
│       └── checkpoint-1125/            # PEFT adapter checkpoint
│       ├── tokenizer.json, config.json
│       └── training_args.bin
│
├── model/
│   └── meta-llama/Llama-2-7b-hf # Hugging Face base model
```
## Data
## RAG Data
![image](https://github.com/user-attachments/assets/8a5d9fe9-3834-4463-a399-f7c712fa82b8)

## Fine Tuning - Static Data
![image](https://github.com/user-attachments/assets/d6be667b-fb30-45dc-a569-7f0b60b35579)


---

## Setup Instructions

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Index the Healthcare Documents**
   ```bash
   cd vectorDB/script
   python index_to_chroma.py
   ```

3. **Run CrewAI Agent Script (Optional)**
   ```bash
   cd agents/scripts
   python patient_report_agent.py
   ```

4. **Launch Streamlit Interface**
   ```bash
   cd streamlit_app
   streamlit run app.py
   ```

---

##  System Configuration

| Setting               | Value        |
|----------------------|--------------|
| GPU                  | A100 (40GB)  |
| Container Disk       | 70GB         |
| Volume Disk          | 200GB        |

**Notes:**
- Fine-tuning with LoRA/QLoRA allows for efficient training on lower VRAM GPUs.
- Volume Disk increase accommodates logs, checkpoints, and datasets.
- Container Disk should be expanded to improve disk I/O during training.

---

##  Model Details

- **Base Model:** [`meta-llama/Llama-2-7b-hf`](https://huggingface.co/meta-llama/Llama-2-7b-hf)
- **PEFT Technique:** LoRA for fine-tuning on healthcare metadata.
- **Embedding Model:** `all-MiniLM-L6-v2` (via `sentence-transformers`)
- **Vector Store:** ChromaDB
- **Agents:** Retriever, Formatter, Email (via `CrewAI`)
- **Frontend:** Streamlit
- **Email Service:** `yagmail`

---

## Output

![image](https://github.com/user-attachments/assets/dccd4f14-b372-4e13-aa3e-66f5bc2b9092)

## Healthcare Limitations
![image](https://github.com/user-attachments/assets/eedca1ff-6bfa-4f27-acc3-5f7136e987f9)

## Mail - Output
![image](https://github.com/user-attachments/assets/08abee19-d22c-424d-b7e4-b8d73ff83aac)



##  Sample Queries

- “What’s the allergy history of patient P0043?”
- “List patients from Block A with asthma.”
- “Who handles IT in Block C?”
- “Send patient summaries to caretaker of P0043.”
- “What’s the janitorial policy in Block A?”

---

##  Future Enhancements

- Integrate with EHR/EMR systems for live data access.
- Add user authentication and role-based access control.
- Extend CrewAI with task delegation (e.g., update records, schedule follow-ups).
- Host the model and app on AWS/GCP with secure APIs.
- Incorporate LangChain, Guardrails, or Azure AI for broader LLM use.

---

## 👤 Author

**Jabinbalan Ravinbalan**  
