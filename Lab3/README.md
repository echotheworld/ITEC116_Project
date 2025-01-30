# Laboratory Activity #3: JSON Processing API

## 📚 Overview
An advanced FastAPI application that demonstrates JSON processing capabilities by integrating with external APIs. This project showcases how to fetch, parse, and transform JSON data from external sources, specifically working with user posts and comments from JSONPlaceholder API.

## 🎯 Objectives
- Master JSON data format manipulation in API development
- Implement JSON parsing and traversal using Python
- Convert Python data structures to JSON format
- Integrate with external REST APIs
- Handle complex nested JSON structures

## 🛠 Technical Requirements
- Python 3.7+
- FastAPI
- Requests library
- JSON module (Python standard library)
- Uvicorn (ASGI server)

## 🚀 Getting Started
1. Clone the repository:
```bash
git clone https://github.com/jpcanamaque/itec116_it4e_lab.git
cd itec116_it4e_lab
cd lab3
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
uvicorn main:app --reload
```

## 📡 API Endpoints

### 1. Get All Posts
```http
GET /posts/
```
Retrieves all posts from JSONPlaceholder API.

#### Query Parameters
| Parameter | Type | Description |
|-----------|------|-------------|
| postId | integer | Optional: Filter posts by specific ID |

### 2. Get Comments
```http
GET /comments/
```
Retrieves comments from JSONPlaceholder API.

#### Query Parameters
| Parameter | Type | Description |
|-----------|------|-------------|
| postId | integer | Optional: Filter comments by post ID |

### 3. Get Formatted Posts
```http
GET /formatted_posts/{userID}
```
Retrieves and formats posts for a specific user.

#### Response Example
```json
{
    "userID": 1,
    "posts": [
        {
            "post_title": "Example Title",
            "post_body": "Example Body"
        }
    ]
}
```

### 4. Get Formatted Comments
```http
GET /formatted_comment/{postID}
```
Retrieves and formats comments for a specific post.

### 5. Get Detailed Post
```http
GET /detailed_post/{userID}
```
Retrieves all posts and their comments for a specific user.

#### Response Structure
```json
{
    "userID": 1,
    "posts": [
        {
            "post_title": "Post Title",
            "post_body": "Post Content",
            "comments": [
                {
                    "postId": 1,
                    "id": 1,
                    "name": "Commenter Name",
                    "email": "commenter@email.com",
                    "body": "Comment Content"
                }
            ]
        }
    ]
}
```

## 💡 Implementation Details
- Integration with JSONPlaceholder API
- Dynamic JSON response formatting
- Error handling for API requests
- Nested JSON structure processing
- Query parameter support

## ⚙️ Technical Architecture
The application leverages:
- FastAPI for API endpoint creation
- Requests library for external API calls
- Native JSON module for data parsing
- Type hints for better code clarity
- HTTPException for error handling

## 🔄 Data Flow
1. Client requests data via endpoint
2. Application calls JSONPlaceholder API
3. JSON response is parsed and processed
4. Data is transformed into required format
5. Formatted response is returned to client

## 🧪 Testing
1. Start the server using the instructions above
2. Access the Swagger UI at `http://127.0.0.1:8000/docs`
3. Test endpoints with different user IDs and post IDs
4. Verify JSON response structure matches requirements

## 👨‍💻 Development Best Practices
- Efficient JSON parsing and manipulation
- Proper error handling for API calls
- Clean code organization
- Comprehensive API documentation
- Type safety with Python type hints

## 📝 License
This project is created as part of ITEC116 coursework.

---

<div align="center">
Made with ❤️ for ITEC116 Laboratory Activity 3
</div> 
