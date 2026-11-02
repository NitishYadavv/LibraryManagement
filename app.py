from flask import Flask, request, jsonify

app = Flask(__name__)

# Book search feature
books = [
    {"id": 1, "name": "Python Programming"},
    {"id": 2, "name": "Data Structures"},
    {"id": 3, "name": "Machine Learning"}
]

def search_book(name):
    return [b for b in books if name.lower() in b["name"].lower()]

# Library fine calculation
def calculate_fine(days):
    if not isinstance(days, int) or isinstance(days, bool) or days < 0:
        raise ValueError("Invalid overdue days")
    return days * 5

@app.route("/")
def home():
    return "Library Management System Running"

@app.route("/search")
def search():
    name = request.args.get("name", "")
    return jsonify(search_book(name))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "admin" and password == "1234":
            return "Login Successful"
        return "Invalid Credentials", 401

    return """
    <form method="POST">
      <input id="username" name="username" placeholder="Username">
      <input id="password" name="password" type="password" placeholder="Password">
      <button id="login" type="submit">Login</button>
    </form>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

def search_by_id(book_id):
    return next((b for b in books if b["id"] == book_id), None)
