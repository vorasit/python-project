class Employee:

    # method
    def detail(self,name,salary,department):
        print("เรียกใช้งาน method class Employee")
        self.name = name
        self.salary = salary
        self.department = department
        print("success define attribute")
        
    def showData(self):
        print("name = {}".format(self.name))
        print("salary = {}".format(self.salary))
        print("department = {}".format(self.department))

# object
obj1 = Employee()
obj1.detail("pin",200000,"programer")
obj1.showData()

obj2 = Employee()
obj2.detail("parn",100000,"ceo")
obj2.showData()

obj3 = Employee()
obj3.detail("pook",20000,"boy")
obj3.showData()

# function
def employee():
    pass