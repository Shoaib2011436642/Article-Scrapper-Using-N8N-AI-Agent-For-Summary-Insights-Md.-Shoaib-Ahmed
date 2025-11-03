# Article-Scrapper-Using-N8N-AI-Agent-For-Summary-Insights-Md.-Shoaib-Ahmed
# 🚀 FastAPI Backend with n8n Integration

This repository contains a FastAPI backend integrated with an n8n workflow.  
Follow the steps below to configure your n8n workflow, run the backend locally on Windows PowerShell, and access the API documentation.

---

## 📋 Prerequisites

- **Python 3.8+** installed on your system  
- **pip** (comes with Python)  
- **n8n** workspace already set up  

---

## 1️⃣ Configure n8n Workflow

1. **Extract Workflow JSON** into your **n8n Workspace**.
2. In the **HTTP Request Node**:
   - Go to **Header Parameters**.
   - Add your Firecrawl API key:  
     ```
     Authorization: Bearer <Your-Firecrawl-API-KEY>
     ```
3. Under the **AI Agent Node**:
   - Check for **Google Gemini Chat Mode**.
   - In **Credentials**, paste your API key generated from **Google AI Studio**.
4. For the **Google Sheets** and **Gmail** nodes:
   - Connect your Google Account to set up the credentials.
5. **Save** the workflow.

---

## 2️⃣ Run the FastAPI Backend in Windows PowerShell

Open **Windows PowerShell** in your project directory and run the following commands:

```powershell
# 1. Create a virtual environment
python -m venv venv

# 2. Activate the virtual environment
venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Start FastAPI with Uvicorn
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

- Use `deactivate` to exit the virtual environment when done.
- If `uvicorn` is not found, install it separately with `pip install uvicorn`.

---

## 3️⃣ Access the FastAPI Swagger UI

Once the server is running, open your browser and navigate to:

```
http://localhost:8000/docs
```

This will open the **FastAPI Swagger UI**, where you can test and interact with all API endpoints.

You can also check the OpenAPI JSON directly at:

```
http://localhost:8000/openapi.json
```

---

## 📝 Notes

- Make sure your `.env` or configuration files (if any) are properly set up.
- If you run into permission issues on Windows, try running PowerShell as Administrator.
- For production, remove `--reload` and configure Uvicorn/Gunicorn accordingly.
