from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

posts = [{
    "title": "Post 1",
    "content": "This is the content of post 1"
},{
    "title": "Post 2",
    "content": "This is the content 2"
}]


@app.get("/articles")
def get_articles():
    return {
        "status": 0,
        "message": "Success",
        "data": {
            "posts": list(reversed(posts))
        }
    }


@app.post("/articles")
def create_article():
    title = request.json.get("title")
    content = request.json.get("content")
    if not title or not content:
        return {
            "status": 1,
            "message": "Missing required fields",
            "data": {}
        }
    post = {
        "title": title,
        "content": content
    }
    posts.append(post)
    return {
        "status": 0,
        "message": "Success",
        "data": {
            "posts": list(reversed(posts))
        }
    }


@app.get("/")
def index():
    return "Hello, World!"


if __name__ == '__main__':
    app.run()
