from locust import HttpLocust, TaskSet, task

class MyTaskSet(TaskSet):
    @task
    def my_task(self):
        self.client.get("/")

class MyLocust(HttpLocust):
    task_set = MyTaskSet
    min_wait = 500
    max_wait = 1000
