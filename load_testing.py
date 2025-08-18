from locust import HttpUser, task, between

class LoadTestUser(HttpUser):
    wait_time = between(1, 2)
    @task
    def test_endpoint(self):
        self.client.get("/api/test")
