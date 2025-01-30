# Laboratory Activity 2: Working with HTTP actions and API parameters

A complete task management system implementing CRUD operations with proper data validation.

## 🎯 Objectives

- Identify and differentiate different ways to parameterize an API
- Discuss HTTP methods and their uses based on best practices
- Use the HTTP methods and parameters to create a simple CRUD simulation API

## 📋 Requirements

### Initial Database
```python
task_db = [
    {"task_id": 1, "task_title": "Laboratory Activity", "task_desc": "Create Lab Act 2", "is_finished": False}
]
```

### Endpoints
- GET `/tasks/{task_id}` - Retrieve a specific task
- POST `/tasks` - Create a new task
- PATCH `/tasks/{task_id}` - Update an existing task
- DELETE `/tasks/{task_id}` - Remove a task

### Response Format
- Success: `{"status": "ok", ...}`
- Error: `{"error": "<error message>"}`

### Validation Requirements
- Null check
- Negative numbers
- Empty strings
- Data type validation

## 💻 Implementation

```python
# Import necessary modules for API functionality
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional

# Initialize the FastAPI application
app = FastAPI()

# Define the structure for a Task
class Task(BaseModel):
    task_id: int = Field(..., gt=0)  # Unique identifier for each task, must be positive
    task_title: str = Field(..., min_length=1)  # Title of the task, cannot be empty
    task_desc: str = Field(..., min_length=1)  # Description of the task, cannot be empty
    is_finished: bool  # Status of the task: completed or not

# Structure for creating a new task
class TaskCreate(BaseModel):
    task_title: str = Field(..., min_length=1)  # Title for the new task
    task_desc: str = Field(..., min_length=1)  # Description for the new task

# Structure for updating an existing task
class TaskUpdate(BaseModel):
    task_title: Optional[str] = Field(None, min_length=1)  # Updated title, if provided
    task_desc: Optional[str] = Field(None, min_length=1)  # Updated description, if provided
    is_finished: Optional[bool] = None  # Updated status, if provided
```

## 🚀 Getting Started

1️⃣ **Clone the repository**
```bash
git clone https://github.com/echotheworld/ITEC116_Project.git
cd ITEC116_Project
cd Lab2
```

2️⃣ **Install dependencies**
```bash
pip install -r requirements.txt
```

3️⃣ **Run the application**
```bash
fastapi run main.py
```

📍 Access the API at `http://127.0.0.1:8000`
📚 API documentation at `http://127.0.0.1:8000/docs`

---

<div align="center">
Made with ❤️ for ITEC116 Course
</div> 
