class Employee:
   def __init__(self,first,last,pay):
    self.first= first
    self.last= last
    self.pay=pay
    self.email= first + "." + last + "@gmail.com"

emp_1=Employee("Joy","Wanjiru",50000)
emp_2=Employee("Vercy","Andrews",70000)

print(emp_1.email)
print(emp_2.email)
       