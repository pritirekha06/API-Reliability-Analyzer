# API Reliability Analyzer

A professional tool to test and monitor API/website reliability with comprehensive metrics.

## Prerequisites
- Python 3.x
- pip package manager

## Installation

### Install all dependencies
```pip install -r requirements.txt```

### Run the server
uvicorn main:app --reload

## How to Use
Enter URL - Any API endpoint or website URL

Set Duration - Test duration in seconds (1-30)

Set RPS - Requests per second (1-5)

Start Test - Click button to begin analysis

View Results - See comprehensive metrics

### Verdict Scale
STABLE - >95% success rate, <0.5s response

DEGRADING - >80% success rate

UNSTABLE - ≤80% success rate

## Disclaimer
Use responsibly. Do not test production systems aggressively.
Default safety limits are in place to prevent accidental overload.
