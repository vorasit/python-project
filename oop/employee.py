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

    def _getIncome(self,bonus=0,overtime=0):
        return (self.__salary * 12)+bonus+overtime

    def __str__(self):
        return ("ชื่อพนักงาน = {} , แผนก = {} , เงินเดือน = {} , รายได้ต่อปี = {}".format(self.__name,self.__department,self.__salary,self._getIncome()))
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

    def __introduce__(self):
        return ("สวัสดีครับผมชือ {}  ทำงานตำแหน่ง = {} ".format(self.__name,self.__department))