import random

from locust import HttpUser, between, task


class JSONPlaceholderUser(HttpUser):
    wait_time = between(1, 3)

    def on_start(self):
        self.user_id = 1
        self.post_ids = [1, 2, 3, 4, 5]

    @task(3)
    def get_users(self):
        self.client.get("/users", params={"userId": self.user_id}, name="/users")

    @task(2)
    def get_comments(self):
        self.client.get(
            "/comments",
            params={"postId": random.choice(self.post_ids)},
            name="/comments",
        )

    @task(5)
    def get_posts(self):
        self.client.get("/posts", params={"userId": self.user_id}, name="/posts")
