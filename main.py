import re
from urllib.parse import urlsplit
from bottle import Bottle, redirect, request, static_file, template


ISSUE_PAGE = "https://github.com/medecau/sevenproxies/issues"


def load_items(path):
    with open(path) as fp:
        return {line.strip() for line in fp}


all_or_patterns = "|".join(load_items("blocklist.txt"))
block = re.compile(f".*(?:{all_or_patterns}).*")
del all_or_patterns

allow = load_items("allowlist.txt")


app = Bottle()


@app.route("/robots.txt")
def robotstxt():
    return static_file("robots.txt")


@app.route("/")
def index():
    return "⚡️"


@app.route("/*/<url:re:.+>")
def index(url):
    url_parts = urlsplit(url)
    allow_redirect = url_parts.hostname in allow

    if not allow_redirect:
        redirect(ISSUE_PAGE)

    user_agent = request.headers.get("User-Agent")

    # the match will return None if we do not recognise the user-agent
    # thus if the match does return something other than None
    # we want to hide the redirect
    hide_redirect = block.match(user_agent.lower()) is not None

    if hide_redirect:
        return f"🖕"

    redirect(url)
