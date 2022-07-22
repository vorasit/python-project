# overloading & overideing
"""
overloading คือ constructor function  ที่มี parameter ที่ต่างกัน
overideing คือ นำ function ของคลาสแม่ นำมาใช้งานที่ subclass และมีการเพิ่มเติมในส่วนของ function แต่ละ subclass ซึ่งแต่ละ subclass มี attribute ที่ต่างกัน
"""
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

class Accounting(Employee):
    __departmentName = "แผนกบัญชี"
    # overloading 
    def __init__(self,name,salary,age):
        super().__init__(name, salary,self.__departmentName)
        self.__age = age

    # overideing
    def _showData(self):
        super()._showData()
        print("age = {}".format(self.__age))
        print("###################################################")
    # overideing
    def __str__(self):
        return (super().__str__()+" อายุ = {}".format(self.__age))

class Programmer(Employee):
    __departmentName = "นักพัฒนาระบบ"
    # overloading 
    def __init__(self,name,salary,experience,skill):
        super().__init__(name, salary, self.__departmentName)
        self.__exp = experience
        self.__skill = skill

    # overideing
    def _showData(self):
        super()._showData()
        print("experience = {}".format(self.__exp))
        print("skill = {}".format(self.__skill))
        print("###################################################")
    # overideing
    def __str__(self):
        return (super().__str__()+" ประสปการณ์ = {} ปี , ทักษะ = {} ".format(self.__exp,self.__skill))

    def __calculateSalary(self):
        pass


class Sale(Employee):
    __departmentName = "ฝ่ายขายสินค้า"
    # overloading 
    def __init__(self,name,salary,area):
        super().__init__(name, salary, self.__departmentName)
        self.__area = area

    # overideing
    def _showData(self):
        super()._showData()
        print("area = {}".format(self.__area))
        print("###################################################")
    # overideing
    def __str__(self):
        return (super().__str__()+" พื้นที่รับผิดชอบ = {} ".format(self.__area))

# object

account = Accounting("pook",20000,30)
#account._showData()
#print(account.__str__())
print("บัญชี รายได้ต่อปี = {} ".format(account._getIncome()))

programmer = Programmer("pin",200000,2,"deverlop ai")
#programmer._showData()
#print(programmer.__str__())
print("โปรแกรมเมอร์ รายได้ต่อปี = {} ".format(programmer._getIncome(5000)))

sale = Sale("parn",100000,"lampang")
#sale._showData()
#print(sale.__str__())
print("ฝ่ายขาย รายได้ต่อปี {} ".format(sale._getIncome()))