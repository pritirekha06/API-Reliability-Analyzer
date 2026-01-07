from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from schemas import TestRequest
from tester import run_test
from analyzer import analyze_results

app = FastAPI(title="API Reliability Analyzer")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/analyze")
async def analyze(test: TestRequest):
    results = await run_test(
        url=str(test.url),
        duration=min(test.duration, 30),
        rps=min(test.rps, 5)
    )
    analysis = analyze_results(results)
    return analysis