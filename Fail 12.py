# 1.  Write a class named Student with two attributes student_id, student_name. Add a new attribute student_class.
#  Create a function to display the entire attribute and their values in Student class.
from fail1 import Peopls

class Student(Peopls):
    def learn(self):
        print('Learning ...')

    def set_class(self, className):
        self.className = className

    def get_class(self):
        return self.className

if __name__ == "__main__":
    p2 = Student(12, "Karen")
    p2.info()
    p2.set_class("First")
    print(p2.get_class())
print("________________________________________________________")
# 2. Create a Vehicle class without any variables and methods
class Vehicle():
    def __init__(self, model, year, ):
        self.model = model
        self.year = year

    def info(self):
        print(f'{self.model}\n{self.year}')

if __name__ == '__main__':
    x1 = Vehicle("BMW", 1994, )
    x1.info()
print('___________________________________________________')
# 3. Write a program to create a Vehicle class with max_speed and mileage instance attributes.
from CLASS import Car

class Vehicle(Car):
    def learn(self):
        print('Learning ...')

    def speed(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

if __name__ == '__main__':
    cra = Vehicle("240km", 40.524)
    cra.info()
print('____________________________________________________________________')
# 4. Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
class S():
    def __init__(self,model,max_speed, mileage):
        self.module = model
        self.max_speed = max_speed
        self.mileage = mileage
    def info(self):
        print(f'{self.module}\n{self.max_speed}\n{self.mileage}')
class Bus(S):
    pass
bus1 =Bus ('Nissan',180, 52.125)
bus1.info()
print('_________________________________________________________________')
# 5. Create a Bus class that inherits from the Vehicle class. Give the capacity argument of Bus.seating_capacity() a default value of 50.
class S():
    def __init__(self,model,max_speed, mileage,capacity):
        self.module = model
        self.max_speed = max_speed
        self.mileage = mileage
        self.capacity = capacity
    def info(self):
        print(f'{self.module}\n{self.max_speed}\n{self.mileage}\n{self.capacity}')
class Bus(S):
    pass
bus2 =Bus ('Nissan',180, 52.125, 50)
bus2.info()
print('___________________________________')