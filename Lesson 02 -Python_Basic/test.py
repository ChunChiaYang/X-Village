class Car():
    __color="blue"
    def __init__(self, wheels_number=4):
        self.wheels_number = wheels_number

class Bus(Car):
    # override __init__ function
    def __init__(self):
        #super().__init__(wheels_number)
        pass
car = Car()
bus = Bus()