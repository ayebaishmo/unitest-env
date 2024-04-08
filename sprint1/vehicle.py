'''
This file holds two classes that holds to classes
They are parent and child class.
# Imagine  I want to list these vehicles on grake's list
# This is a parent class is the more generic of the two
'''


class Vehicle:
    '''
    This is class doc string
    '''
    def __init__(self, make, model, color, year, mileage):
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        self.mileage = mileage

    def honk(self):
        return "HOOOOOOOOOOONK"
    
    def drive(self, miles_drivem):
        self.mileage = self.mileage + miles_drivem
        return self.mileage
    
    def __repr__(self):
        return f'''A {self.color} {self.year} {self.make} 
                    {self.model} with {self.mileage} mile'''


# if __name__ == "__main__":
#     my_vehicle = Vehicle('Toyota', 'comfy', 'gray', 2015, 6000)

#     print(my_vehicle.make)
#     print(my_vehicle.mileage)

#     print(my_vehicle.honk())
#     print(my_vehicle.drive(1234))
#     print(my_vehicle.mileage)

#     print(my_vehicle)


class Convertible(Vehicle):
    '''
    This is class doc string
    # imagine  I want to list these vehicles on grake's list
    # The more specific class
    # The Convertible class inherits from Vehicle
    '''
    def __init__(self, make, model, color, year, mileage, top_down = True):
        super().__init__(make, model, color, year, mileage)
        self.top_down = top_down


    def change_top_status(self):
        if self.top_down:
            self.top_down = False
            return "Top is now up!"
        else:
            self.top_down = True
            return "Top is now down"
    def __repr__(self):
        return f'''A {self.color} {self.year} {self.make} {self.model} with {self.mileage} mile'''


if __name__ == "__main__":
    Convertible_1 = Convertible('Toyota', 'comfy', 'gray', 2015, 6000)

    # print(my_vehicle.make)
    # print(my_vehicle.mileage)

    # print(my_vehicle.honk())
    # print(my_vehicle.drive(1234))
    # print(my_vehicle.mileage)

    # print(my_vehicle)
    # we are accessing convertible methods
    print(Convertible_1.top_down)
    print(Convertible_1.change_top_status())
    print(Convertible_1.top_down)
    # we are access vehicle methods and attributes
    print(Convertible_1.honk())
    print(Convertible_1.drive(1234))
