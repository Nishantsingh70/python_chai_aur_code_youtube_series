class Car:
    total_car = 0

    def __init__(self, brand, model):
        ## making the attribute/property private.
        self.__brand = brand
        self.__model = model
        # self.total_car +=1 #=> It is also correct method we can do it also.
        Car.total_car += 1

    ## getter method
    def get_brand(self):
        return self.__brand + " !"

    ## setter method
    def set_brand(self, brand):
        self.__brand = brand

    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    @staticmethod
    def general_description():
        return "Cars are means of transport"
    
    @property
    def model(self):
        return self.__model
    


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric charge"


# creating object from class and accessing class properties and methods.
my_car = Car("Toyota", "Corolla")
print(my_car.brand)
print(my_car.model)
print(my_car.full_name())

my_new_car = Car("Tata", "Safari")
print(my_new_car.model)

# Encapsulation => setter and getter methods access.
my_tesla = ElectricCar("Tesla", "Model S", "85kWh")
my_tesla.set_brand("Tata")
print(my_tesla.get_brand())

# polymorphism
safari = Car("Tata", "Safari")
print(safari.fuel_type())

# Find total cars created from the Car class.
print(Car.total_car)
print(my_tesla.total_car)

# static method => to make the function/property not to access by any object of the class.
print(safari.general_description())
print(Car.general_description())

# property method => to make the attribute read only.
my_car_two = Car("Tata", "Safari")
my_car_two.model = "City"
print(my_car_two.model)

# instanceof
print(isinstance(my_tesla, Car))
print(isinstance(my_tesla, ElectricCar))

# print(my_tesla.__brand)
# print(my_tesla.fuel_type())


# Multiple inheritance
class Battery:

    def battery_info(self):
        return "this is battery"

class Engine:

    def engine_info(self):
        return "This is engine"

class ElectricCarTwo(Battery, Engine, Car):
    pass

my_new_tesla = ElectricCarTwo("Tesla", "Model S")
print(my_new_tesla.engine_info())
print(my_new_tesla.battery_info())