import redis
from locust import HttpUser, task, between, events
from locust.runners import WorkerRunner

USER_COUNTER_KEY = "user_counter"

redis_client = redis.Redis(host = "locust-redis", port = 6380, db = 0)

@events.test_start.add_listener
def on_test_start(environment, **_kwargs):
    if not isinstance(environment.runner, WorkerRunner):
        redis_client.delete(USER_COUNTER_KEY)


class WebsiteUser(HttpUser):

    wait_time = between(1, 5)

    def on_start(self):
        user_count = redis_client.incr(USER_COUNTER_KEY)
        self.username = f"user{user_count}"

    @task
    def task(self):
        print(self.username)

