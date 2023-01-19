from CLASS import Car
class Vehicle(Car):
    def learn(self):
        print('Learning ...')
    def speed(self,max_speed,mileage):
        self.max_speed = max_speed
        self.mileage = mileage

if __name__== '__main__':
    cra = Vehicle("240km", 40.524)
    cra.info()
