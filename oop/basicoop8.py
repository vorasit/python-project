class Employee:

    # class variablr
    minSalary = 12000
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

class Accounting(Employee):
    __departmentName = "แผนกบัญชี"
    def __init__(self):
        pass

class Programmer(Employee):
    __departmentName = "นักพัฒนาระบบ"
    def __init__(self):
        pass
class Sale(Employee):
    __departmentName = "ฝ่ายขายสินค้า"
    def __init__(self):
        pass
# object

account = Accounting()
print(account.minSalary)
print(account._maxSalary)

programmer = Programmer()
sale = Sale()

