from locust import HttpUser, task, constant

class TestStressUser(HttpUser):
    wait_time = constant(0.1)
    @task
    def test_endpoint(self):
        self.client.get("/api/test")

