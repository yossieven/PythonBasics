import random

from locust import HttpUser, task, between


class TestUser(HttpUser):
    wait_time = between(1, 3)
    host = "http://localhost:8082/employee"
    employees = ('Yossi', 'Adi', 'Moshe', 'Natan' 'Shavit', 'Ella', 'Vered', 'Dan', 'Yoram', 'Sveta')
    programs = ('java', 'ruby', 'basic', 'C', 'C-sharp', '.NET')

    def get_random_employee(self):
        employee_indx = random.randint(0, 9)
        return self.employees[employee_indx]

    @task
    def get_employee(self):
        employee_name = self.get_random_employee()
        self.client.get(f"?name={employee_name}", name="/name")

    @task
    def get_birthday_employee(self):
        month = random.randint(1, 12)
        self.client.get(f"/birthday?month={month}", name="/birthday")

    @task
    def patch_employee_percentage(self):
        percentage = random.randint(1, 100)
        employee_name = self.get_random_employee()
        self.client.patch(f"?name={employee_name}&percentage={percentage}", name="/percentage")

    @task
    def patch_employee_salary(self):
        salary = random.randint(1000, 40000)
        employee_name = self.get_random_employee()
        self.client.patch(f"?name={employee_name}&salary={salary}", name="/salary")


    @task
    def patch_employee_program(self):
        program_index = random.randint(0, 5)
        program = self.programs[program_index]
        employee_name = self.get_random_employee()
        self.client.patch(f"?name={employee_name}&program={program}", name="/program")
