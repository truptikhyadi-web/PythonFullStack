class Employee():
    def __init__(self, name, employee_id, base_salary):
        self.name=name
        self.employee_id=employee_id
        self.base_salary=base_salary
    def calculate_pay(self):
        return self.base_salary
    def get_details(self):
        return f"{self.name} ({self.employee_id})"
    def __str__(self):
        return self.get_details()

class Manager(Employee):
    def __init__(self, name, employee_id, base_salary,team_size):
        super().__init__(name, employee_id, base_salary)
        self.team_size=team_size
    def calculate_pay(self):
        return self.base_salary+(self.team_size*500)
    def get_details(self):
        return f"{self.name} ({self.employee_id}) - Manager"

class Developer(Employee):
    def __init__(self, name, employee_id, base_salary, programming_language):
        super().__init__(name, employee_id, base_salary)
        self.programming_language=programming_language
    def calculate_pay(self):
        if self.programming_language in["Python", "GO"]:
            return self.base_salary + 1000
        else:
            return self.base_salary
    def get_details(self):
        return f"{self.name} ({self.employee_id}) - Developer"

class Intern(Employee):
    def __init__(self, name, employee_id, base_salary, stipend):
        super().__init__(name, employee_id, base_salary)
        self.stipend=stipend
    def calculate_pay(self):
        return self.stipend
    def get_details(self):
        return f"{self.name} ({self.employee_id}) - Intern"

def generate_payroll(employees):
    for emp in employees:
        print(f"{emp.get_details()}: ${emp.calculate_pay()}")

employees=[
    Manager("Asha", "M001", 60000, team_size=5),
    Developer("Ravi", "D001", 50000, "Python"),
    Intern("Zoe", "I001", 0, stipend=15000)
]
generate_payroll(employees)   


    



        
    
   
