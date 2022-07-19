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
obj1.name = "pinzaa"
obj1.salary = 500000
obj1.showData()

obj2 = Employee("parn",100000,"ceo")
obj2.showData()

obj3 = Employee("pook",20000,"boy")
obj3.showData()