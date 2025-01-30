# Laboratory Activity #4: Advanced API Implementation

## 📚 Overview
An advanced FastAPI application demonstrating professional API development practices including versioning, authentication, and proper HTTP status code handling. This project builds upon the To-Do List API from Laboratory Activity #2, implementing multiple API versions and secure authentication.

## 🎯 Objectives
- Implement API versioning (v1 and v2)
- Add API key authentication
- Handle HTTP exceptions properly
- Manage environment variables securely
- Apply REST API best practices

## 🛠 Technical Requirements
- Python 3.7+
- FastAPI
- python-dotenv
- Pydantic
- Uvicorn (ASGI server)

## 🔐 Security Setup
1. Create a `.env` file in the root directory:
```bash
API_KEY=your_api_key_here
```

2. Add `.env` to your `.gitignore`:
```bash
# .gitignore
.env
__pycache__/
.venv/
```

## 🚀 Getting Started
1. Clone the repository:
```bash
git clone https://github.com/echotheworld/ITEC116_Project.git
cd ITEC116_Project
cd Lab4
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

### API Version 1 (No Authentication)

#### 1. Get Tasks
```http
GET /apiv1/tasks?task_id={task_id}
```
- Status Code 200: Success
- Status Code 204: No tasks found
- Status Code 404: Task not found

#### 2. Create Task
```http
POST /apiv1/tasks
```
- Status Code 201: Task created

#### 3. Update Task
```http
PATCH /apiv1/tasks/{task_id}
```
- Status Code 204: Task updated
- Status Code 404: Task not found

#### 4. Delete Task
```http
DELETE /apiv1/tasks/{task_id}
```
- Status Code 204: Task deleted
- Status Code 404: Task not found

### API Version 2 (With Authentication)

All v2 endpoints require an API key in the header:
```http
X-API-Key: your_api_key_here
```

#### 1. Get Tasks
```http
GET /apiv2/tasks?task_id={task_id}
```

#### 2. Create Task
```http
POST /apiv2/tasks
```

#### 3. Update Task
```http
PATCH /apiv2/tasks/{task_id}
```

#### 4. Delete Task
```http
DELETE /apiv2/tasks/{task_id}
```

## 🔒 Authentication
- API Key required for all v2 endpoints
- Key must be provided in request header
- Invalid or missing key returns 403 Forbidden

## 📊 HTTP Status Codes
| Code | Description | Usage |
|------|-------------|-------|
| 200 | OK | Successful GET request |
| 201 | Created | Successful task creation |
| 204 | No Content | Successful update/delete or no tasks |
| 400 | Bad Request | Invalid input |
| 403 | Forbidden | Invalid/missing API key |
| 404 | Not Found | Task not found |

## 💡 Implementation Details
- Dual API versions (v1 and v2)
- Environment variable management
- Comprehensive error handling
- Status code implementation
- Secure API key validation

## ⚙️ Technical Architecture
The application uses:
- FastAPI for API framework
- python-dotenv for environment variables
- Pydantic models for data validation
- FastAPI security for API key authentication
- HTTPException for error handling

## 🧪 Testing
1. Start the server using the instructions above
2. Test v1 endpoints without authentication
3. Test v2 endpoints with API key
4. Verify proper status codes
5. Test error scenarios

## 👨‍💻 Development Best Practices
- Secure API key handling
- Proper HTTP status codes
- Clean code organization
- Comprehensive error handling
- Type safety with Pydantic

## 📝 License
This project is created as part of ITEC116 coursework.

---

<div align="center">
Made with ❤️ for ITEC116 Laboratory Activity 4
</div> 
