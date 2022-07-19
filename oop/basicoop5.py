class Employee:
    # constructor
    # privae method
    def __init__(self,name,salary,department):
        # private attribute
        self._name = name #protected
        self.__salary = salary
        self.__department = department
        #self._showData()

    #protectes method    
    def _showData(self):
        print("name = {}".format(self._name))
        print("salary = {}".format(self.__salary))
        print("department = {}".format(self.__department))

    def __del__(self):
        print("Call Destructor")

# object
obj1 = Employee("pin",200000,"programer")
obj2 = Employee("parn",100000,"ceo")

obj3 = Employee("pook",20000,"boy")
obj3._name = 'ko'
obj3.__salary = 30000
obj3._showData()

