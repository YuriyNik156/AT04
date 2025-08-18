from locust import HttpUser, task, between, LoadTestShape

class SpikeTestUser(HttpUser):
    wait_time = between(1, 2)
    @task
    def test_endpoint(self):
        self.client.get("/api/test")

class SpikeLoadShape(LoadTestShape):
    def tick(self):
        run_time = self.get_run_time()
        if run_time < 30:
            return (10, 1)
        elif run_time < 35:
            return (200, 1)
        elif run_time < 70:
            return (10, 1)
        else:
            return None
