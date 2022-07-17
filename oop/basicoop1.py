class Employee:
    

    # method

    def detail(self):
        print("เรียกใช้งาน method class Employee")
        self.name = "pin"
        self.salary = 200000
        print("success define attribute")
        print("name = {}".format(self.name))
        print("salary = {}".format(self.salary))

# object
emp1 = Employee()
emp1.detail()


# function
def employee():
    pass