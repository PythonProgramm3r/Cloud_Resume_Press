# Serverless AI Personal Agent (RAG Architecture)

### **Live Demo:** [Click Here to Chat with the Agent](https://my-streamlit-service-1042834751077.us-central1.run.app/)

## 📋 Project Overview
This project is a **Serverless Retrieval-Augmented Generation (RAG)** application designed to modernize the recruitment experience. Instead of reading a static PDF resume, recruiters can interrogate a **Generative AI Agent** to ask specific questions about my technical experience, architectural philosophy, and background.

This application demonstrates the bridge between **Legacy Data** (static text files) and **Modern Cloud Architecture** (Containerized Microservices on Google Cloud).

## 🏗️ Architecture

The system follows a standard microservice pattern, containerized with Docker and deployed to Google Cloud Run for auto-scaling and zero-maintenance infrastructure.

```mermaid
graph LR
    User[Recruiter/User] -- HTTPS --> CloudRun[Google Cloud Run Container]
    subgraph "Microservice Logic (Python)"
        CloudRun -- Streamlit --> UI[Frontend Interface]
        UI -- Query --> Logic[Context Injection Engine]
        Logic -- Read --> Docs[Local Knowledge Base (Resume/Ethos)]
        Logic -- API Call --> Vertex[Google Vertex AI (Gemini Pro)]
    end
    Vertex -- Generative Response --> User
