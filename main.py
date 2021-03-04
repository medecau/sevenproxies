from bottle import Bottle, redirect, static_file, template


app = Bottle()


@app.route("/robots.txt")
def robotstxt():
    return static_file("robots.txt")


@app.route("/")
def index():
    return "⚡️"


@app.route("/*/<url:re:.+>")
def index(url):
    redirect(url)
