# `requests` is a module that enables users to perform API calls
# You can download this by doing pip install requests (or just install the requirements.txt file that comes with this code.)
import requests

# `json` is native module in Python that enables users to parse JSON strings into Python data types (list, dictionary, tuples, etc.)
# and vice versa. This is a native module so there is no need to install this as this comes with the installation of Python
import json 

# FastAPI imports
from fastapi import FastAPI, HTTPException
from typing import Optional

# Instantiates the FastAPI class
app = FastAPI()

# Example # 1: We are trying to get the values from an external API. We used a query parameter to make the API scalable to different API calls
# to the external API
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

# Example #2: : We are trying to get the values from an external API. We used a path parameter to ensure that we are requiring the parameter.
# After calling the API, we format the data according to our preference by accessing the values of the JSON string.
@app.get("/formatted_posts/{userID}")
def get_post_then_format_according_to_user(userID: Optional[int] = None):
    # We get the data from the get_post function above. In this case, we are calling it as a function.
    posts = get_posts()

    # Create the new format of data that we want to present
    data = {"userID": userID, "posts": []}

    # Enumerate the posts, then filter the user ID based on the parameter
    # Then add it to the `posts` value
    for idx, u in enumerate(posts):

        # Take note here that in Python, to get the value of a key in a dictionary, we use the [] notation
        # where in the string inside the [] is the key of the value in the dictionary.
        if u['userId'] == userID:
            data["posts"].append({
                "post_title": u["title"],
                "post_body": u["body"],
            })
    return data

@app.get("/formatted_comment/{postID}")
def get_post_then_format_according_to_user(postID: int):
    # We get the data from the get_comments function above. In this case, we are calling it as an API
    req = requests.get(f'http://127.0.0.1:8000/comments/?postId={postID}')
    comments = json.loads(req.text)

    # Create the new format of data that we want to present
    data = {"post_id": postID, "comments": []}

    # Enumerate the comments, then filter the post ID based on the parameter
    # Then add it to the `comments` value
    for idx, c in enumerate(comments):
        # Take note here that in Python, to get the value of a key in a dictionary, we use the [] notation
        # where in the string inside the [] is the key of the value in the dictionary.
        if c['postId'] == postID:
            data["comments"].append({
                "commenter_email": c["email"],
                "commenter_name": c["name"],
                "comment": c["body"],
            })
    return data

@app.get("/detailed_post/{userID}")
def get_detailed_post(userID: int):
    # Retrieve all posts from the external API
    posts = get_posts()
    
    # Filter the posts to only include those matching the given userID
    user_posts = [post for post in posts if post['userId'] == userID]
    
    # Check if any posts were found for the given userID
    # If not, raise a 404 error with an informative message
    if not user_posts:
        raise HTTPException(status_code=404, detail=f"User with ID {userID} not found or has no posts")
    
    # Initialize the response data structure
    data = {"userID": userID, "posts": []}
    
    # Iterate through each post belonging to the user
    for post in user_posts:
        # Retrieve all comments associated with the current post
        post_comments = get_comments(post['id'])
        
        # Create a dictionary containing the post's details and its comments
        post_data = {
            "post_title": post["title"],
            "post_body": post["body"],
            "comments": post_comments
        }
        
        # Append the post data to the posts list in our response structure
        data["posts"].append(post_data)
    
    # Return the complete data structure containing all posts and their comments
    return data
