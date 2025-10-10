#!/usr/bin/python3
from task_02_requests import fetch_and_print_posts, fetch_and_save_posts

if __name__ == "__main__":
    ok = fetch_and_print_posts()
    print("-- saved -->", fetch_and_save_posts("posts.csv"))
