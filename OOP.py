class Employee:
    
    def __init__(self, name ,age, id):
        self.name=name
        self.age= age    
        self.id= id
    
    def display():
        print("This is a trial of functions")
        
        
Employee1= Employee("Dennis ", 20,14599)
print(Employee1.name)
print(Employee1.id)
print(Employee1.age)

#Employee1.display()
print("=========================================")

# This class is the child class of the class Employee.
# It inherits the methods from the Employee class.
class Employer(Employee):        

    Employer1= Employee("John",30, 1000)
    print(Employer1.name)
    print(Employer1.id)
    print(Employer1.age)
    
print("==========================================")
