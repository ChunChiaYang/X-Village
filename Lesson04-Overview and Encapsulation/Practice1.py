class Car:
    def __init__(self,color,speed=0):
        self.color=color
        self.speed=0
        
    def boost(self):
        self.speed=self.speed+1

    def step_break(self):
        self.speed=self.speed-1
    
    def get_speed(self):
        return self.speed
    
    def set_speed(self,newspeed):
        if newspeed<0 or newspeed>100:
            return "error"
        else:
            self.speed=newspeed
            return self.speed

car1=Car("red")
car1.boost()
print(car1.get_speed())
car1.step_break()
print(car1.get_speed())
print(car1.set_speed(-2))
print(car1.set_speed(50))
print(car1.set_speed(110))



