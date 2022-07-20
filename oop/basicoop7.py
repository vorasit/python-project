class Employee:

    # class variable
    _minSalary = 12000
    _maxSalary = 1200000
    
    # constructor
    # privae method
    def __init__(self,name,salary,department):
        # private attribute
        # instance variable
        self.__name = name 
        self.__salary = salary
        self.__department = department
        #self._showData()

    #protectes method    
    def _showData(self):
        print("name = {}".format(self.getName()))
        print("salary = {}".format(self.getSalary()))
        print("department = {}".format(self.getDepartment()))

    def __del__(self):
        print("Call Destructor")

    # setter method
    def setName(self,newname):
        self.__name = newname

    def setSalary(self,newsalary):
        self.__salary = newsalary
    
    def setDepartment(self,newdepartment):
        self.__department = newdepartment

    # getter method
    def getName(self):
        return self.__name

    def getSalary(self):
        return self.__salary

    def getDepartment(self):
        return self.__department
# object
obj1 = Employee("pin",200000,"programer")
obj2 = Employee("parn",100000,"ceo")

obj3 = Employee("pook",20000,"boy")

obj1.setName("pinzaa")
obj1.setSalary(300000)
obj1.setDepartment("deverloper")
print("พนักงานดีเด่น = {} ".format(obj1.getName()))
obj1._showData()
print("เงินเดือนต่ำสุดของพนักงาน = "+str(Employee._minSalary))