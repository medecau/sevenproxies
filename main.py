from bottle import Bottle, static_file, template


app = Bottle()


@app.route("/robots.txt")
def robotstxt():
    return static_file("robots.txt")


@app.route("/")
def index():
    return "⚡️"
