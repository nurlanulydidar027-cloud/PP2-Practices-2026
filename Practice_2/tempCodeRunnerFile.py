class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary
    
    def total_salary(self):
        return float(self.base_salary)
    
class Manager(Employee):
    def __init__(self, name, base_salary, bonus_percent):
        super().__init__(name, base_salary)
        self.bonus_percent = int(bonus_percent)

    def total_salary(self):
        return self.base_salary * (1 + self.bonus_percent / 100)
    
class Developer(Employee):
    def __init__(self, name, base_salary, completed_projects):
        super().__init__(name, base_salary)
        self.completed_projects = int(completed_projects)

    def total_salary(self):
        return self.base_salary + self.completed_projects * 500
    
class Intern(Employee):
    pass

line = input().split()
post = line[0]
name = line[1]
salary = line[2]

if post == "Manager":
    obj = Manager(name, salary, line[3])
elif post == "Developer":
    obj = Developer(name, salary, line[3])    
else:
    obj = Intern(name, salary)

print(f"Name: {obj.name}, Total: {obj.total_salary():.2f}")