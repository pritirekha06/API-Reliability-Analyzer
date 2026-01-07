# API Reliability Analyzer

A web-based testing tool that monitors API and website performance by checking response reliability, measuring speed, and analyzing consistency over repeated requests.

## Prerequisites
- Python 3.x
- pip package manager

### Install all dependencies
```
pip install -r requirements.txt
```

### Run the server
```
uvicorn main:app --reload
```

## How to Use
- Enter URL - Any API endpoint or website URL

- Set Duration - Test duration in seconds (1-30)

- Set RPS - Requests per second (1-5)

- Start Test - Click button to begin analysis

- View Results - See comprehensive metrics

## What You'll See
- Total requests sent during the test

- Success rate percentage of successful responses

- Response times including average and maximum durations

- Reliability verdict - STABLE, DEGRADING, or UNSTABLE based on performance thresholds

### Verdict Scale
- ``STABLE`` - >95% success rate, <0.5s response

- ``DEGRADING`` - >80% success rate

- ``UNSTABLE`` - ≤80% success rate

## Disclaimer
Use this tool responsibly - don't aggressively test live services, respect API rate limits, and be mindful that excessive requests can impact server performance.

