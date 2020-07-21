from locust import User, task, between


class TestBookStore(User):

    wait_time = between(1, 3)

