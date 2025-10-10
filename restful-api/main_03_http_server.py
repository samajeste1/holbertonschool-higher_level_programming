#!/usr/bin/python3
# Lance le serveur et visite http://localhost:8000, /data, /status avec le navigateur ou curl.
from task_03_http_server import run

if __name__ == "__main__":
    run(port=8000)
