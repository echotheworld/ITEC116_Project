# Laboratory Activity #1: Introduction to FastAPI ➗

A fundamental FastAPI application implementing factorial calculations with specific requirements.

## 🎯 Objectives

- Introduce FastAPI as a technology stack for developing API
- Review Python as a programming language for API development
- Create, run, and test APIs created using FastAPI
- Practice logic building and technical expertise through coding

## 📋 Requirements

- Written in FastAPI
- Endpoint Name: `/factorial/{starting_number}`
- Endpoint Logic:
  - Compute the factorial of the inputted value
  - If the value inputted is 0, return `{"result": false}`
  - Implement using a while loop

## 💻 Implementation

```python
from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/factorial/{value}")
def calculate_factorial(value: int):
    if value < 0:
        return {"error": "Value must be a non-negative integer."}
    
    if value == 0:
        return {"result": False}  # Return false for input value of 0

    factorial = 1
    counter = 1

    while counter <= value:
        factorial *= counter
        counter += 1

    return {"result": factorial}
```

## 🚀 Getting Started

1️⃣ **Clone the repository**
```bash
git clone https://github.com/echotheworld/ITEC116_Project.git
cd ITEC116_Project
cd Lab1
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
