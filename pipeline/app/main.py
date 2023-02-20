from flask import Flask, render_template, request

app = Flask("Simple Flask App")


# create a new route to return a string
@app.route("/")
def home():
    return f"/ => {request.query_string}"


# create a new route to return html
@app.route("/html")
def html():
    return "<h1>hello world!</h1>"


# create a new route to return json
@app.route("/json")
def json2():
    return {"hello": "world"}


# create a new route to return a rendered template
@app.route("/template")
def template():
    return render_template("index.html", message="hello world!")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
