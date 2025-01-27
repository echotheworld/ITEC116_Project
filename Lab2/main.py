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

# Initial database of tasks
task_db = [
    {"task_id": 1, "task_title": "Laboratory Activity", "task_desc": "Create Lab Act 2", "is_finished": False}
]

# GET endpoint to retrieve a specific task
@app.get("/tasks/{task_id}")
def read_task(task_id: int):
    # Validate that the task_id is positive
    if task_id <= 0:
        raise HTTPException(status_code=400, detail={"error": "Task ID must be a positive integer"})
    # Search for the task in the database
    task = next((task for task in task_db if task["task_id"] == task_id), None)
    if task:
        return {"status": "ok", "task": task}  # Return the task if found
    raise HTTPException(status_code=404, detail={"error": "Task not found"})  # Raise an error if not found

# POST endpoint to create a new task
@app.post("/tasks")
def create_task(task: TaskCreate):
    # Generate a new task ID
    if not task_db:
        new_task_id = 1
    else:
        new_task_id = max(task["task_id"] for task in task_db) + 1
    # Create and add the new task to the database
    new_task = Task(task_id=new_task_id, **task.dict(), is_finished=False)
    task_db.append(new_task.dict())
    return {"status": "ok", "task": new_task}  # Return the newly created task

# PATCH endpoint to update an existing task
@app.patch("/tasks/{task_id}")
def update_task(task_id: int, task_update: TaskUpdate):
    # Validate that the task_id is positive
    if task_id <= 0:
        raise HTTPException(status_code=400, detail={"error": "Task ID must be a positive integer"})
    # Find the task in the database
    task_index = next((index for index, task in enumerate(task_db) if task["task_id"] == task_id), None)
    if task_index is not None:
        # Update the task with new information
        updated_task = {**task_db[task_index], **task_update.dict(exclude_unset=True)}
        # Ensure title and description are not empty after update
        if updated_task["task_title"] is None or updated_task["task_desc"] is None:
            raise HTTPException(status_code=400, detail={"error": "Task title and description cannot be empty"})
        task_db[task_index] = updated_task
        return {"status": "ok", "task": updated_task}  # Return the updated task
    raise HTTPException(status_code=404, detail={"error": "Task not found"})  # Raise an error if task not found

# DELETE endpoint to remove a task
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    # Validate that the task_id is positive
    if task_id <= 0:
        raise HTTPException(status_code=400, detail={"error": "Task ID must be a positive integer"})
    # Find the task in the database
    task_index = next((index for index, task in enumerate(task_db) if task["task_id"] == task_id), None)
    if task_index is not None:
        # Remove the task if found
        deleted_task = task_db.pop(task_index)
        return {"status": "ok", "deleted_task": deleted_task}  # Return the deleted task
    raise HTTPException(status_code=404, detail={"error": "Task not found"})  # Raise an error if task not found