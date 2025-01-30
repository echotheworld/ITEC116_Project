# FastAPI Laboratory Collection 🚀

<div align="center">

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Render](https://img.shields.io/badge/Render-%46E3B7.svg?style=for-the-badge&logo=render&logoColor=white)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

</div>

<p align="center">
A comprehensive collection of FastAPI laboratory activities demonstrating various aspects of modern API development - from basic calculations to cloud deployment.
</p>

---

## 📚 Laboratory Activities Overview

<details>
<summary><b>Laboratory Activity #1: Introduction to FastAPI</b> ➗</summary>

A fundamental FastAPI application implementing factorial calculations with specific requirements.

### Key Features
- 🔹 RESTful endpoint `/factorial/{starting_number}`
- 🔹 Efficient while loop implementation
- 🔹 Special case handling (returns `{"result": false}` for input 0)
- 🔹 Input validation for negative numbers
- 🔹 Performance-optimized calculation

### Technical Implementation
- Endpoint validates input for non-negative integers
- Uses while loop for factorial calculation
- Returns JSON response with calculation result
- Includes error handling for invalid inputs

### Learning Outcomes
- FastAPI basics and endpoint creation
- Python programming fundamentals
- API testing and validation
- Logic building in API context
</details>

<details>
<summary><b>Laboratory Activity 2: Working with HTTP actions and API parameters</b> ✅</summary>

A complete task management system implementing CRUD operations with proper data validation.

### Key Features
- 🔹 Full CRUD functionality (Create, Read, Update, Delete)
- 🔹 Pydantic models for data validation
- 🔹 In-memory task database
- 🔹 Standardized JSON responses

### Endpoints
- GET `/tasks/{task_id}` - Retrieve a specific task
- POST `/tasks` - Create a new task
- PATCH `/tasks/{task_id}` - Update an existing task
- DELETE `/tasks/{task_id}` - Remove a task

### Technical Implementation
- Implements proper data validation using Pydantic models
- Maintains consistent response format
- Includes error handling for all operations
- Uses in-memory storage with proper data structure
</details>

<details>
<summary><b>Laboratory Activity #3: Working with JSON</b> 📊</summary>

Advanced implementation focusing on JSON data handling and external API integration.

### Key Features
- 🔹 External API integration
- 🔹 Complex JSON data processing
- 🔹 Nested data structure handling
- 🔹 Detailed post and comment relationships

### Key Endpoints
- GET `/detailed_post/{userID}` - Retrieves all posts and comments for a user
- GET `/posts/` - Fetches posts with optional filtering
- GET `/comments/` - Retrieves comments with post filtering

### Technical Implementation
- Integrates with JSONPlaceholder API
- Implements proper error handling
- Processes and transforms complex JSON data
- Maintains efficient data traversal
</details>

<details>
<summary><b>Laboratory Activity #4: Advanced API Implementation</b> 🔐</summary>

Enterprise-level implementation featuring versioning and security features.

### Key Features
- 🔹 API versioning (v1 & v2)
- 🔹 API key authentication
- 🔹 Environment variable management
- 🔹 Comprehensive HTTP status handling

### Technical Highlights
- Two API versions with different security levels
- Proper HTTP status codes implementation
- Environment-based configuration
- Secure API key validation

### Security Features
- API key authentication in v2 endpoints
- Environment variable management
- Secure error handling
- Protected routes and operations
</details>

<details>
<summary><b>Laboratory Activity #5: Deploying API in Cloud</b> ☁️</summary>

Final implementation demonstrating cloud deployment capabilities using Render.

### Key Features
- 🔹 Cloud deployment on Render
- 🔹 Production-ready configuration
- 🔹 API documentation
- 🔹 Secure environment variable handling

### Deployment Details
- Hosted on Render platform
- Custom domain configuration
- Environment variable management
- Interactive Swagger documentation

### Access Points
- Base URL: `https://itec116-feolino.onrender.com/`
- API Documentation: `https://itec116-feolino.onrender.com/docs`
</details>

## 🛠️ Technology Stack

- **Framework:** FastAPI
- **Language:** Python 3.8+
- **Documentation:** Swagger/OpenAPI
- **Deployment:** Render
- **Environment Management:** python-dotenv
- **Data Validation:** Pydantic

## 🚀 Getting Started

1️⃣ **Clone the repository**
```bash
git clone https://github.com/YOUR_USERNAME/ITEC116_Labs.git
```

2️⃣ **Set up virtual environment**
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3️⃣ **Install dependencies**
```bash
pip install -r requirements.txt
```

4️⃣ **Configure environment variables**
```bash
# Create .env file and add required variables
API_KEY=your_api_key_here
```

5️⃣ **Run the application**
```bash
uvicorn main:app --reload
```

📍 Access the API at `http://127.0.0.1:8000`
📚 API documentation at `http://127.0.0.1:8000/docs`

## 📂 Project Structure

```
ITEC116_Labs/
├── lab1/                 # Factorial Calculator API
├── lab2/                 # Todo List API
├── lab3/                 # JSON Processing API
├── lab4/                 # Advanced API Implementation
├── lab5/                 # Cloud Deployment
├── requirements.txt      # Project dependencies
└── README.md            # Project documentation
```

## 🔒 Security Considerations

- API keys are managed through environment variables
- Sensitive data is never committed to the repository
- Authentication is required for protected endpoints
- Proper error handling and status codes

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<div align="center">
Made with ❤️ for ITEC116 Course
</div> 
