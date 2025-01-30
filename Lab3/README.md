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

## 💻 Implementation Details

### External API Integration
The application uses JSONPlaceholder API for data:
- **Posts API**: `https://jsonplaceholder.typicode.com/posts`
  - Returns list of posts with user IDs
- **Comments API**: `https://jsonplaceholder.typicode.com/comments`
  - Returns comments for specific posts

### Endpoint Documentation

1. **Get Posts**
   - **Endpoint**: `/posts`
   - **Method**: GET
   - **Optional Parameters**: 
     - `postId` (query parameter): Filter by specific post ID

2. **Get Comments**
   - **Endpoint**: `/comments`
   - **Method**: GET
   - **Optional Parameters**:
     - `postId` (query parameter): Filter comments by post ID

3. **Get Detailed Post**
   - **Endpoint**: `/detailed_post/{userID}`
   - **Method**: GET
   - **Parameters**:
     - `userID` (path parameter): ID of the user to fetch posts for

### Example Usage

1. **Get all posts for a user with their comments**:
```bash
curl http://127.0.0.1:8000/detailed_post/1
```
Response:
```json
{
    "userID": 1,
    "posts": [
        {
            "post_title": "sunt aut facere repellat provident",
            "post_body": "quia et suscipit suscipit recusandae...",
            "comments": [
                {
                    "postId": 1,
                    "id": 1,
                    "name": "id labore ex et quam laborum",
                    "email": "Eliseo@gardner.biz",
                    "body": "laudantium enim quasi est quidem..."
                },
                // ... more comments
            ]
        },
        // ... more posts
    ]
}
```

2. **Get specific post**:
```bash
curl http://127.0.0.1:8000/posts?postId=1
```
Response:
```json
{
    "userId": 1,
    "id": 1,
    "title": "sunt aut facere repellat provident",
    "body": "quia et suscipit suscipit recusandae..."
}
```

3. **Get comments for a post**:
```bash
curl http://127.0.0.1:8000/comments?postId=1
```
Response:
```json
[
    {
        "postId": 1,
        "id": 1,
        "name": "id labore ex et quam laborum",
        "email": "Eliseo@gardner.biz",
        "body": "laudantium enim quasi est quidem..."
    },
    // ... more comments
]
```

### Error Handling

1. **User Not Found**:
```bash
curl http://127.0.0.1:8000/detailed_post/999
```
Response:
```json
{
    "detail": "User with ID 999 not found or has no posts"
}
```

2. **Invalid User ID**:
```bash
curl http://127.0.0.1:8000/detailed_post/abc
```
Response:
```json
{
    "detail": "Invalid user ID format"
}
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
