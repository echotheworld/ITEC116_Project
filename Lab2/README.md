# Laboratory Activity #2: To-Do List API

## 📚 Overview
A comprehensive To-Do List API built with FastAPI, implementing CRUD operations with proper HTTP methods and parameter handling. This project demonstrates best practices in API development, including data validation, error handling, and RESTful principles.

## 🎯 Objectives
- Implement different HTTP methods (GET, POST, PATCH, DELETE)
- Master API parameterization techniques
- Create a CRUD-based API system
- Practice proper error handling and validation
- Apply REST API best practices

## 🛠 Technical Requirements
- Python 3.7+
- FastAPI
- Pydantic
- Uvicorn (ASGI server)

## 🚀 Getting Started
1. Clone the repository:
```bash
git clone https://github.com/echotheworld/ITEC116_Project.git
cd ITEC116_Project
cd Lab2
```

2. Set up virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # For Unix/macOS
# or
.venv\Scripts\activate     # For Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
fastapi run main.py
```

## 📡 API Endpoints

### 1. Get Task
```http
GET /tasks/{task_id}
```
Retrieves a specific task by ID.

#### Parameters
| Parameter | Type | Description |
|-----------|------|-------------|
| task_id | integer | The unique identifier of the task (must be positive) |

#### Response Example
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

### 2. Create Task
```http
POST /tasks
```
Creates a new task.

#### Request Body
```json
{
    "task_title": "New Task",
    "task_desc": "Task Description"
}
```

### 3. Update Task
```http
PATCH /tasks/{task_id}
```
Updates an existing task.

#### Request Body
```json
{
    "task_title": "Updated Title",
    "task_desc": "Updated Description",
    "is_finished": true
}
```

### 4. Delete Task
```http
DELETE /tasks/{task_id}
```
Removes a task by ID.

## 💡 Implementation Details
- Comprehensive data validation using Pydantic models
- Error handling with appropriate HTTP status codes
- In-memory task database with initial seed data
- Input validation for all endpoints
- Proper response formatting

## ⚙️ Technical Architecture
The application uses:
- FastAPI for robust API development
- Pydantic models for data validation
- Type hints for better code clarity
- HTTPException for error handling
- BaseModel inheritance for data structures

## 🔒 Data Models

### Task Model
```python
{
    "task_id": int,       # Positive integer
    "task_title": str,    # Non-empty string
    "task_desc": str,     # Non-empty string
    "is_finished": bool   # Task completion status
}
```

## 🧪 Testing
1. Start the server using the instructions above
2. Access the Swagger UI documentation at `http://127.0.0.1:8000/docs`
3. Test endpoints using the interactive Swagger interface
4. Verify proper error handling and validation

## 👨‍💻 Development Best Practices
- Input validation for all parameters
- Proper error messages and status codes
- Clean code organization
- Comprehensive API documentation
- Type safety with Pydantic models

## 📝 License
This project is created as part of ITEC116 coursework.

---

<div align="center">
Made with ❤️ for ITEC116 Laboratory Activity 2
</div> 
