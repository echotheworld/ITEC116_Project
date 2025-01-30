# Laboratory Activity #4: Advanced API Implementation 🔐

Enterprise-level implementation featuring versioning, authentication, and proper HTTP status code handling.

## 🎯 Objectives

- Implement versioning, authentication, and proper HTTP exception handling in developing API
- Implement best practices in handling environment variables

## 📋 Requirements

### API Versioning
- Version 1: `/apiv1/tasks`
- Version 2: `/apiv2/tasks` (with API key authentication)

### HTTP Status Codes
1. Error Cases (404):
   - Task not found in list
   - Delete non-existent task
   - Update non-existent task

2. Success Cases:
   - Task added (201)
   - Task updated (204)
   - Task deleted (204)
   - No tasks found (204)
   - General success (200)

### Authentication
- API key required for v2 endpoints
- Key stored in `.env` file
- `.gitignore` configuration to exclude `.env`

## 💻 Implementation

```python
from fastapi import FastAPI, HTTPException, Depends, Header
from fastapi.security.api_key import APIKey
from pydantic import BaseModel, Field
from typing import Optional, List
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
API_KEY = os.getenv("API_KEY")

app = FastAPI()

# API Key authentication
async def get_api_key(api_key: str = Header(None)):
    if api_key is None or api_key != API_KEY:
        raise HTTPException(
            status_code=403,
            detail="Invalid or missing API Key"
        )
    return api_key

# Example v1 endpoint (no authentication)
@app.get("/apiv1/tasks", status_code=200)
def read_task_v1(task_id: Optional[int] = None):
    if task_id is not None:
        if task_id <= 0:
            raise HTTPException(status_code=400, detail={"error": "Task ID must be a positive integer"})
        task = next((task for task in task_db if task["task_id"] == task_id), None)
        if task:
            return {"status": "ok", "task": task}
        raise HTTPException(status_code=404, detail={"error": "Task not found"})
    
    if not task_db:
        raise HTTPException(status_code=204, detail={"error": "No tasks found"})
    return {"status": "ok", "tasks": task_db}

# Example v2 endpoint (with authentication)
@app.get("/apiv2/tasks", status_code=200)
def read_task_v2(task_id: Optional[int] = None, api_key: APIKey = Depends(get_api_key)):
    return read_task_v1(task_id)
```

## 🚀 Getting Started

1️⃣ **Clone the repository**
```bash
git clone https://github.com/echotheworld/ITEC116_Project.git
cd ITEC116_Project
cd Lab4
```

2️⃣ **Install dependencies**
```bash
pip install -r requirements.txt
```

3️⃣ **Configure environment**
```bash
# Create .env file (DO NOT COMMIT THIS FILE)
touch .env

# Create .gitignore
echo ".env" > .gitignore
```

Add your API key to the `.env` file:
- Create a secure API key (recommended: at least 32 characters)
- Never share your API key
- Format in .env file: `API_KEY=your_secret_key`

4️⃣ **Run the application**
```bash
fastapi run main.py
```

📍 Access the API at `http://127.0.0.1:8000`
📚 API documentation at `http://127.0.0.1:8000/docs`

## 🔑 Authentication

⚠️ **Security Notes:**
- Keep your API key secret
- Never commit the `.env` file
- Regenerate the key if compromised
- Use HTTPS in production
- Implement rate limiting for security

To use v2 endpoints:
1. Add your API key to the request header
2. Use proper authorization in all v2 endpoint calls
3. Handle 403 errors for invalid/missing keys

---

<div align="center">
Made with ❤️ for ITEC116 Course
</div> 
