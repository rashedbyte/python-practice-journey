class Vehicle:

    def __init__(self, brand):

        self.brand = brand


    def start(self):

        print(f"{self.brand} is tarting")


class Car(Vehicle):

    pass



car1=Car("Mercedes M8")

car1.start() 