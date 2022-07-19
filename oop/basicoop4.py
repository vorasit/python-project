class Employee:
    # constructor
    # privae method
    def __init__(self,name,salary,department):
        # protectes attribute
        self._name = name
        self._salary = salary
        self._department = department
        #self._showData()

    #protectes method    
    def _showData(self):
        print("name = {}".format(self._name))
        print("salary = {}".format(self._salary))
        print("department = {}".format(self._department))

    def __del__(self):
        print("Call Destructor")

# object
obj1 = Employee("pin",200000,"programer")
obj2 = Employee("parn",100000,"ceo")

obj3 = Employee("pook",20000,"boy")
obj3._name = 'ko'
obj3._salary = 30000
obj3._showData()