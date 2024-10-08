import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, Response

from .txexpl import TxExplainer

txe = TxExplainer("eth")

STATIC = os.path.join(os.path.dirname(__file__), "static")

INDEX_PATH = os.path.join(STATIC, "index.html")
MD_PATH = os.path.join(STATIC, "markdown.html")
JS_PATH = os.path.join(STATIC, "index.js")
MONKEY_PATH = os.path.join(STATIC, "monkey.js")

URL_BASE = "URL_BASE"
conf = {URL_BASE: "http://localhost:8081"}

app = FastAPI()

# Enable CORS for all routes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", response_class=HTMLResponse)
def index():
    data = open(INDEX_PATH).read().replace(URL_BASE, conf[URL_BASE])
    return data


@app.get("/index.js")
def index_js():
    data = open(JS_PATH).read().replace(URL_BASE, conf[URL_BASE])
    return Response(content=data, media_type="text/javascript")


@app.get("/monkey.js")
def monkey_js():
    data = open(MONKEY_PATH).read().replace(URL_BASE, conf[URL_BASE])
    return Response(content=data, media_type="text/javascript")


@app.get("/explain_url", response_class=HTMLResponse)
def explain_url(url):
    msg = txe.gen_full_md_from_url(url)
    msg = msg.replace("`", "\\`")
    return open(MD_PATH).read().replace("#MARKDOWN", str(msg))


@app.get("/explain_txid", response_class=HTMLResponse)
def explain_txid(chain, txid):
    txe.switch_chain(chain)
    msg = txe.gen_full_md_from_txid(txid)
    msg = msg.replace("`", "\\`")
    return open(MD_PATH).read().replace("#MARKDOWN", str(msg))


@app.get("/explain_call", response_class=HTMLResponse)
def explain_call(chain, to, data, value=0):
    txe.switch_chain(chain)
    msg = txe.gen_full_md_from_call(to, data, value)
    msg = msg.replace("`", "\\`")
    return open(MD_PATH).read().replace("#MARKDOWN", str(msg))
