from employee import Employee

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
