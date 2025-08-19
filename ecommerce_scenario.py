from locust import HttpUser, task, between

class EcommerceUser(HttpUser):
    vait_time = between(1, 3)

    @task(1)
    def login(self):
        response = self.client.post(
            "/api/login",
            data = {"username" : "testuser", "password" : "testpass"}
        )
        if response.status_code == 200:
            self.token = response.json().get("token")

    @task(2)
    def get_products(self):
        self.client.get("/api/products")

    @task(1)
    def add_to_card(self):
        headers = {"Authorization": f"Bearer {self.