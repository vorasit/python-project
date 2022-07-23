from employee import Employee
from accounting import Accounting
from programmer import Programmer
from sale import Sale


account = Accounting("pook",20000,30)
account.setName("Lnwzaa")
account._showData()
#print(account.__str__())
print("บัญชี รายได้ต่อปี = {} ".format(account._getIncome()))

programmer = Programmer("pin",200000,2,"deverlop ai")
#programmer._showData()
#print(programmer.__str__())
print("โปรแกรมเมอร์ รายได้ต่อปี = {} ".format(programmer._getIncome(5000)))
print(programmer.__introduce__())

sale = Sale("parn",100000,"lampang")
#sale._showData()
#print(sale.__str__())
print("ฝ่ายขาย รายได้ต่อปี {} ".format(sale._getIncome()))