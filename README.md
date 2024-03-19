# Mai-Invoice-Generator

## Description

This is a Python project using FastAPI for creating a web API and Poetry for dependency management.

## Installation

This project uses [Poetry](https://python-poetry.org/) for dependency management. If you haven't installed it yet,
follow the instructions on their website.

To set up and start the project, follow these steps:

```bash
# Clone the repository
git clone <your-repo-link>
cd <your-repo-name>

# Install dependencies
poetry install
poetry shell # Activate the Poetry environment

# run the app from the project root directory
(mai-invoice-generator-py3.12) ➜  Mai-Invoice-Generator git:(master) pwd
/Users/maihome/Mai-Invoice-Generator
(mai-invoice-generator-py3.12) ➜  Mai-Invoice-Generator git:(master) uvicorn mai-invoice-generator.main
:app --host 0.0.0.0 --port 8080 --reload
INFO:     Will watch for changes in these directories: ['/Users/maihome/Mai-Invoice-Generator']
INFO:     Uvicorn running on http://0.0.0.0:8080 (Press CTRL+C to quit)
INFO:     Started reloader process [43322] using WatchFiles
INFO:     Started server process [43324]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     127.0.0.1:51321 - "GET / HTTP/1.1" 200 OK
INFO:     127.0.0.1:51321 - "GET /favicon.ico HTTP/1.1" 404 Not Found
INFO:     127.0.0.1:51323 - "GET /docs HTTP/1.1" 200 OK
INFO:     127.0.0.1:51323 - "GET /openapi.json HTTP/1.1" 200 OK
```
