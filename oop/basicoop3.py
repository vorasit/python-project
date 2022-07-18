class Employee:
    # constructor
    def __init__(self,name,salary,department):
        self.name = name
        self.salary = salary
        self.department = department

        
    def showData(self):
        print("name = {}".format(self.name))
        print("salary = {}".format(self.salary))
        print("department = {}".format(self.department))

    def __del__(self):
        print("Call Destructor")

# object
obj1 = Employee("pin",200000,"programer")
obj2 = Employee("parn",100000,"ceo")
obj3 = Employee("pook",20000,"boy")
# chek abount obj == class employee
a = isinstance(obj1, Employee)
print(a)

print(dir(obj1)) # detail have to method in this class
print(obj1.__class__) # <class '__main__.Employee'> tell abount obj this class
