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

## 💻 Implementation Details

### Data Models
- **Task**: The main data structure for tasks
  - `task_id`: Positive integer
  - `task_title`: Non-empty string
  - `task_desc`: Non-empty string
  - `is_finished`: Boolean

### Endpoint Documentation

1. **Get Task**
   - **Endpoint**: `/tasks/{task_id}`
   - **Method**: GET
   - **Parameters**: 
     - `task_id` (path parameter): Positive integer

2. **Create Task**
   - **Endpoint**: `/tasks`
   - **Method**: POST
   - **Request Body**:
     ```json
     {
       "task_title": "string",
       "task_desc": "string"
     }
     ```

3. **Update Task**
   - **Endpoint**: `/tasks/{task_id}`
   - **Method**: PATCH
   - **Parameters**:
     - `task_id` (path parameter): Positive integer
   - **Request Body** (all fields optional):
     ```json
     {
       "task_title": "string",
       "task_desc": "string",
       "is_finished": boolean
     }
     ```

4. **Delete Task**
   - **Endpoint**: `/tasks/{task_id}`
   - **Method**: DELETE
   - **Parameters**:
     - `task_id` (path parameter): Positive integer

### Example Usage

1. **Get a specific task**:
```bash
curl http://127.0.0.1:8000/tasks/1
```
Response:
```json
{
    "status": "ok",
    "task": {
        "task_id": 1,
        "task_title": "Laboratory Activity",
        "task_desc": "Create Lab Act 2",
        "is_finished": false
    }
}
```

2. **Create a new task**:
```bash
curl -X POST http://127.0.0.1:8000/tasks \
  -H "Content-Type: application/json" \
  -d '{"task_title": "New Task", "task_desc": "Task Description"}'
```
Response:
```json
{
    "status": "ok",
    "task": {
        "task_id": 2,
        "task_title": "New Task",
        "task_desc": "Task Description",
        "is_finished": false
    }
}
```

3. **Update a task**:
```bash
curl -X PATCH http://127.0.0.1:8000/tasks/1 \
  -H "Content-Type: application/json" \
  -d '{"is_finished": true}'
```
Response:
```json
{
    "status": "ok",
    "task": {
        "task_id": 1,
        "task_title": "Laboratory Activity",
        "task_desc": "Create Lab Act 2",
        "is_finished": true
    }
}
```

4. **Delete a task**:
```bash
curl -X DELETE http://127.0.0.1:8000/tasks/1
```
Response:
```json
{
    "status": "ok",
    "message": "Task deleted successfully"
}
```

### Error Handling

1. **Task Not Found**:
```bash
curl http://127.0.0.1:8000/tasks/999
```
Response:
```json
{
    "error": "Task not found"
}
```

2. **Invalid Input**:
```bash
curl -X POST http://127.0.0.1:8000/tasks \
  -H "Content-Type: application/json" \
  -d '{"task_title": "", "task_desc": ""}'
```
Response:
```json
{
    "error": "Validation error: task_title and task_desc cannot be empty"
}
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
