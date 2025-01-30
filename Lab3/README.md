# Laboratory Activity #3: Working with JSON 📊

Advanced implementation focusing on JSON data handling and external API integration.

## 🎯 Objectives

- Familiarize and identify JSON as a primary data format for API development
- Parse JSON strings and traverse data in the JSON string using Python
- Convert Python data structures into a valid JSON format

## 📋 Requirements

### Endpoint Specification
- Endpoint: `/detailed_post/{userID}`
- Method: GET
- Functionality: Show all posts of a specific user and all comments per each post
- Response: Use appropriate key names based on the value output

### External API Integration
The application integrates with JSONPlaceholder API endpoints:
- Posts: `https://jsonplaceholder.typicode.com/posts`
- Comments: `https://jsonplaceholder.typicode.com/comments`

## 💻 Implementation

```python
# Import necessary modules
import requests
import json 
from fastapi import FastAPI, HTTPException
from typing import Optional

app = FastAPI()

@app.get("/posts/")
def get_posts(postId: Optional[int] = None):
    if postId is None:
        posts = requests.get('https://jsonplaceholder.typicode.com/posts')
        response = json.loads(posts.text)
    else:
        posts = requests.get(f'https://jsonplaceholder.typicode.com/posts/{postId}')
        response = json.loads(posts.text)
    return response

@app.get("/comments/")
def get_comments(postId: Optional[int] = None):
    if postId is None:
        comments = requests.get('https://jsonplaceholder.typicode.com/comments')
        response = json.loads(comments.text)
    else:
        comments = requests.get(f'https://jsonplaceholder.typicode.com/comments/?postId={postId}')
        response = json.loads(comments.text)
    return response

@app.get("/detailed_post/{userID}")
def get_detailed_post(userID: int):
    # Retrieve all posts from the external API
    posts = get_posts()
    
    # Filter posts by userID
    user_posts = [post for post in posts if post['userId'] == userID]
    
    if not user_posts:
        raise HTTPException(status_code=404, detail=f"User with ID {userID} not found or has no posts")
    
    # Prepare response data
    data = {"userID": userID, "posts": []}
    
    # Get posts with comments
    for post in user_posts:
        post_comments = get_comments(post['id'])
        post_data = {
            "post_title": post["title"],
            "post_body": post["body"],
            "comments": post_comments
        }
        data["posts"].append(post_data)
    
    return data
```

## 🚀 Getting Started

1️⃣ **Clone the repository**
```bash
git clone https://github.com/echotheworld/ITEC116_Project.git
cd ITEC116_Project
cd Lab3
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
