from flask import Flask, render_template, request

app = Flask(__name__, template_folder="templates")


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("form.html")
    elif request.method == "POST":
        print(request.form.keys())
        if "username" in request.form.keys() and "password" in request.form.keys():
            username = request.form.get("username")
            password = request.form.get("password")
            return {"msg": f"hello there {username}"}
        else:
            return {"error": "Invalid request"}
        
@app.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "GET":
        return render_template("upload-form.html")
    elif request.method == "POST":
        print(request.form.keys())
        if "username" in request.form.keys() and "password" in request.form.keys():
            username = request.form.get("username")
            password = request.form.get("password")
            return {"msg": f"hello there {username}"}
        else:
            return {"error": "Invalid request"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
