import re
from bottle import Bottle, redirect, request, static_file, template


app = Bottle()

with open("blocklist.txt") as fp:
    blocklist = {line.strip() for line in fp}

all_or_patterns = "|".join(blocklist)
block = re.compile(f".*(?:{all_or_patterns}).*")


@app.route("/robots.txt")
def robotstxt():
    return static_file("robots.txt")


@app.route("/")
def index():
    return "⚡️"


@app.route("/*/<url:re:.+>")
def index(url):
    user_agent = request.headers.get("User-Agent")

    # the match will return None if we do not recognise the user-agent
    # thus if the match does return something other than None
    # we want to hide the redirect
    hide_redirect = block.match(user_agent.lower()) is not None

    if hide_redirect:
        return f"🖕"

    redirect(url)
