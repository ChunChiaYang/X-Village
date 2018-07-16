class Animal():
    def __init__(self,feet=4):
        self.feet_number=feet

    def shout(self):
        print("Hello! I'm an animal")

class Dog(Animal):
    pass

dog = Dog()
print(dog.feet_number) 
dog.shout() 