from employee import Employee

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

    def __introduce__(self):
        print(super().__introduce__()+" ผมมีรับผิดชอบเขต = {}".format(self.__area))

    def setName(self,newname):
        super().setName(newname)

    def setSalary(self,newsalary):
        super().setSalary(newsalary)
    
    def setDepartment(self,newdepartment):
        super().setDepartment(newdepartment)

    # getter method
    def getName(self):
        return super().getName()

    def getSalary(self):
        return super().getSalary()

    def getDepartment(self):
        return super().getDepartment()