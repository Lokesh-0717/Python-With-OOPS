class Animal():
    def Eat(self):
        print("Eating")
class Dog():
    def Speak(self):
        print("Barking")
class Mammel(Animal,Dog):
    def Walk(self):
        print("Walking")
m1=Mammel()
m1.Eat()
m1.Speak()
m1.Walk()
