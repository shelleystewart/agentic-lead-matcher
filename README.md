# agentic-lead-matcher
[Watch the 120-Second NotebookLM Video Demo Here] 

https://github.com/user-attachments/assets/693765c8-aaf8-4491-a149-c04ebd966603

Custom Multi-Agent Video Demo

https://github.com/user-attachments/assets/c5f50660-56aa-4063-b912-cb023aa2621c

Local, multi-agent real estate lead qualifier using Streamlit and Llama 3.2 via Ollama to prove how a brokerage's inventory management and copywriting workflows can be safely automated.
# Local Real Estate Agentic Workflow (Powered by Ollama)

A lightweight, local multi-agent system built to streamline real estate operations by automatically parsing incoming client leads, matching them against an inventory database, and drafting tailored follow-up copy. 

This project was built as a targeted prototype demonstrating localized AI workflows tailored for modern brokerage environments.

## Features
- **Multi-Agent Architecture:** Features two specialized agents—an *Inventory Specialist* to query data structures and a *Real Estate Copywriter* to handle communications.
- **100% Local Execution:** Configured to run entirely on-device using **Ollama (`llama3.2:1b`)** via an OpenAI-compatible local server API, ensuring zero API costs and absolute data privacy.
- **Interactive UI:** A clean interface built with **Streamlit** for real-time lead ingestion and execution tracing.

## Tech Stack
- **Language:** Python
- **LLM Orchestration:** OpenAI Python SDK (pointed to local host)
- **Local Model:** Ollama (`llama3.2:1b`)
- **Frontend/UI:** Streamlit

## How to Run Locally
1. Install requirements: `pip install streamlit openai`
2. Start the local model server: `ollama run llama3.2:1b`
3. Run the application: `streamlit run app.py`
