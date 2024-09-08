from locust import HttpUser, constant, task

class SiteUsers(HttpUser):
    wait_time = constant(1)

    @task
    def load_homepage(self):
        self.client.get("/")

    @task
    def load_search(self):
        self.client.get("/searchplayerurl")

    @task
    def load_add(self):
        self.client.get("/addplayerurl")

    @task
    def load_delete(self):
        self.client.get("/deleteplayerurl")

    @task
    def load_update(self):
        self.client.get("/updateplayerurl")

    @task
    def load_report(self):
        self.client.get("/playersreporturl")