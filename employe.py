class Employee:
    # A data member to count the number of Employees is created
    Empcount = 0
    
    # A constructor is created to initialize name, family, salary, department
    def _init_(self, name, family, salary, department):
        self.name = name
        self.family = family
        self.salary = salary
        self.department = department
        Employee.Empcount += 1
    
    # Function to average salary
    def average_salary(self):
        return self.salary / Employee.Empcount

# Another class Fulltime Employee is created and it inherits the properties of Employee class
class FulltimeEmployee(Employee):
    pass

# Creating the instances of Fulltime Employee class and Employee class 
e1 = Employee("rithvik", "reddy", 9000, "IT")
e2 = FulltimeEmployee("prathyusha", "bose", 8000, "CS")


# Calling functions
print(e1.average_salary())
print(e2.average_salary())