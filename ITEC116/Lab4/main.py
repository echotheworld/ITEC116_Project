# Import necessary modules for API functionality
from fastapi import FastAPI, HTTPException, Depends, Header
from fastapi.security.api_key import APIKey
from pydantic import BaseModel, Field
from typing import Optional, List
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API key from environment variable
API_KEY = os.getenv("API_KEY")

# Initialize the FastAPI application
app = FastAPI()

# API Key authentication dependency
async def get_api_key(api_key: str = Header(None)):
    if api_key is None or api_key != API_KEY:
        raise HTTPException(
            status_code=403,
            detail="Invalid or missing API Key"
        )
    return api_key

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

# Initial database of tasks
task_db = [
    {"task_id": 1, "task_title": "Laboratory Activity", "task_desc": "Create Lab Act 2", "is_finished": False}
]

# Version 1 router
@app.get("/apiv1/tasks", status_code=200)
def read_task_v1(task_id: Optional[int] = None):
    # If task_id is provided, find specific task
    if task_id is not None:
        if task_id <= 0:
            raise HTTPException(status_code=400, detail={"error": "Task ID must be a positive integer"})
        task = next((task for task in task_db if task["task_id"] == task_id), None)
        if task:
            return {"status": "ok", "task": task}
        raise HTTPException(status_code=404, detail={"error": "Task not found"})
    
    # If task_id is not provided (getting all tasks)
    if not task_db:
        raise HTTPException(status_code=204, detail={"error": "No tasks found"})
    return {"status": "ok", "tasks": task_db}

@app.post("/apiv1/tasks", status_code=201)
def create_task_v1(task: TaskCreate):
    # Generate a new task ID
    if not task_db:
        new_task_id = 1
    else:
        new_task_id = max(task["task_id"] for task in task_db) + 1
    # Create and add the new task to the database
    new_task = Task(task_id=new_task_id, **task.dict(), is_finished=False)
    task_db.append(new_task.dict())
    return {"status": "ok", "task": new_task}  # Return the newly created task

@app.patch("/apiv1/tasks/{task_id}", status_code=204)
def update_task_v1(task_id: int, task_update: TaskUpdate):
    # Validate that the task_id is positive
    if task_id <= 0:
        raise HTTPException(status_code=400, detail={"error": "Task ID must be a positive integer"})
    # Find the task in the database
    task_index = next((index for index, task in enumerate(task_db) if task["task_id"] == task_id), None)
    if task_index is None:
        raise HTTPException(status_code=404, detail={"error": "Task not found"})
    
    # Update the task with new information
    updated_task = {**task_db[task_index], **task_update.dict(exclude_unset=True)}
    # Ensure title and description are not empty after update
    if updated_task["task_title"] is None or updated_task["task_desc"] is None:
        raise HTTPException(status_code=400, detail={"error": "Task title and description cannot be empty"})
    task_db[task_index] = updated_task
    return None  # 204 No Content

@app.delete("/apiv1/tasks/{task_id}", status_code=204)
def delete_task_v1(task_id: int):
    # Validate that the task_id is positive
    if task_id <= 0:
        raise HTTPException(status_code=400, detail={"error": "Task ID must be a positive integer"})
    # Find the task in the database
    task_index = next((index for index, task in enumerate(task_db) if task["task_id"] == task_id), None)
    if task_index is None:
        raise HTTPException(status_code=404, detail={"error": "Task not found"})
    # Remove the task if found
    deleted_task = task_db.pop(task_index)
    return None  # 204 No Content

# Version 2 endpoints with authentication
@app.get("/apiv2/tasks", status_code=200)
def read_task_v2(task_id: Optional[int] = None, api_key: APIKey = Depends(get_api_key)):
    return read_task_v1(task_id)

@app.post("/apiv2/tasks", status_code=201)
def create_task_v2(task: TaskCreate, api_key: APIKey = Depends(get_api_key)):
    return create_task_v1(task)

@app.patch("/apiv2/tasks/{task_id}", status_code=204)
def update_task_v2(task_id: int, task_update: TaskUpdate, api_key: APIKey = Depends(get_api_key)):
    return update_task_v1(task_id, task_update)

@app.delete("/apiv2/tasks/{task_id}", status_code=204)
def delete_task_v2(task_id: int, api_key: APIKey = Depends(get_api_key)):
    return delete_task_v1(task_id)