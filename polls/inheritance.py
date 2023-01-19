class Animal:  
     def speak(self):  
            print("Animal Speaking")  
    #child class Dog inherits the base class Animal  
     class Dog(Animal):  
        def bark(self):  
            print("dog barking")  
d = Dog()  
d.bark()  
d.speak() 
class Person:
    def happy(self):
        print("veryone is happy")

person= Person()
person.happy()

class School:
    pupils = 500
    teachers = 400

    def total(self):
        mytotal=self.pupils + self.teachers
        return("The total", mytotal)
school=School()
school.total()
