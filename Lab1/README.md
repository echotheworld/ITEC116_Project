# Laboratory Activity #1: FastAPI Factorial Calculator

## 📚 Overview
This project is a FastAPI-based web service that calculates the factorial of a given number. It serves as an introduction to API development using FastAPI and Python, demonstrating fundamental concepts in web service implementation.

## 🎯 Objectives
- Implement a FastAPI-based web service
- Practice Python programming for API development
- Create and test RESTful endpoints
- Develop efficient algorithmic solutions
- Gain hands-on experience with modern API development

## 🛠 Technical Requirements
- Python 3.7+
- FastAPI
- Uvicorn (ASGI server)

## 🚀 Getting Started
1. Clone the repository:
```bash
git clone https://github.com/echotheworld/ITEC116_Project.git
cd ITEC116_Project
cd Lab1
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
fastapi run main.py
```

## 📡 API Endpoint

### Factorial Calculation
```http
GET /factorial/{starting_number}
```

#### Parameters
|     Parameter   |   Type  |             Description               |
|-----------------|---------|---------------------------------------|
| starting_number | integer | The number to calculate factorial for |

#### Response Examples

##### Successful Calculation
```json
{
    "result": 120  // Example for input 5
}
```

##### Zero Input
```json
{
    "result": false
}
```

##### Error Case
```json
{
    "error": "Value must be a non-negative integer."
}
```

## 💡 Implementation Details
- Uses a while loop for factorial calculation
- Includes input validation for negative numbers
- Special handling for zero input
- Efficient computation method
- JSON response format

## ⚙️ Technical Architecture
The application is built using:
- FastAPI framework for API development
- Python's type hinting for parameter validation
- RESTful architecture principles
- Efficient algorithmic implementation

## 🧪 Testing
To test the API:
1. Start the server using the instructions above
2. Access the API at `http://localhost:8000/factorial/{number}`
3. Use the interactive Swagger documentation at `http://localhost:8000/docs`

## 👨‍💻 Development
This project follows best practices for:
- Code organization
- Error handling
- Input validation
- API documentation

## 📝 License
This project is created as part of ITEC116 coursework.

---

<div align="center">
Made with ❤️ for ITEC116 Laboratory Activity
</div> 
