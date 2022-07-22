from employee import Employee

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