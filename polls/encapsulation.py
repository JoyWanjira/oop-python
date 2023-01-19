class Intern:
    def __init__(self,name,project,salary):
        self.name = name
        self.project = project
        self.salary =salary

    def show(self):
     print("Name:" ,self.salary,"salary:" ,self.salary)

    def work(self):
     print(self.name,"is working on", self.project)   

int_1= Intern("Joy","OOP",1000) 

int_1.show()
int_1.work()