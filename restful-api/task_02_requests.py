#!/usr/bin/python3
"""task_02_requests

Fetch posts from JSONPlaceholder, print titles and save posts to posts.csv.
"""

import csv
import requests


def fetch_and_print_posts():
    """Fetch posts and print HTTP status and all titles."""
    url = "https://jsonplaceholder.typicode.com/posts"
    resp = requests.get(url, timeout=10)
    print("Status Code:", resp.status_code)
    if resp.status_code != 200:
        return False
    try:
        posts = resp.json()
    except ValueError:
        return False
    for p in posts:
        print(p.get("title"))
    return True


def fetch_and_save_posts(csv_filename="posts.csv"):
    """Fetch posts and save id,title,body to csv_filename. Returns True on success."""
    url = "https://jsonplaceholder.typicode.com/posts"
    resp = requests.get(url, timeout=10)
    if resp.status_code != 200:
        return False
    try:
        posts = resp.json()
    except ValueError:
        return False
    rows = [{"id": p.get("id"), "title": p.get("title"), "body": p.get("body")}
            for p in posts]
    try:
        with open(csv_filename, "w", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for r in rows:
                writer.writerow(r)
        return True
    except Exception:
        return False
