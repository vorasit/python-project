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