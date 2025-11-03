from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr, HttpUrl
import os
import uuid
import httpx
from dotenv import load_dotenv

load_dotenv()  # reads .env in project root

N8N_WEBHOOK_URL = os.getenv("N8N_WEBHOOK_URL")  # set this to the *FULL* n8n webhook URL (test or production)
if not N8N_WEBHOOK_URL:
    raise RuntimeError("Please set N8N_WEBHOOK_URL in your .env file")

app = FastAPI(title="AI Agent Bridge")

# allow local dev to call this backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Submission(BaseModel):
    email: EmailStr
    article_url: HttpUrl


@app.get("/health")
async def health():
    return {"ok": True}


@app.post("/submit")
async def submit(payload: Submission):
    """Accepts JSON { email, article_url } → generate session_id → forward to n8n webhook

    Returns JSON { ok: True, session_id }
    """
    session_id = str(uuid.uuid4())
    body = {
        "email": payload.email,
        "article_url": str(payload.article_url),
        "session_id": session_id,
    }

    async with httpx.AsyncClient() as client:
        try:
            resp = await client.post(N8N_WEBHOOK_URL, json=body, timeout=20)
            resp.raise_for_status()
        except httpx.HTTPError as e:
            # convert to a 502 so the frontend knows the forward failed
            raise HTTPException(status_code=502, detail=f"Failed to forward to n8n: {str(e)}")

    return {"ok": True, "session_id": session_id}