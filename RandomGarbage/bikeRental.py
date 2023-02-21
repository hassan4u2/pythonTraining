'''
# Bike rental system

'''

# customer class


class Customer:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # setters
    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    # getters
    def get_name(self):
        return self.name

    def get_age(self):
        return self.age


# main class
class Bike:
    def __init__(self, name, price, maxSpeed):
        self.name = name
        self.price = price
        self.maxSpeed = maxSpeed

    # setters
    def set_name(self, name):
        self.name = name

    def set_price(self, price):
        self.price = price

    def set_maxSpeed(self, maxSpeed):
        self.maxSpeed = maxSpeed

    # getters
    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def get_maxSpeed(self):
        return self.maxSpeed


# inherit from Bike
class ElectricBike(Bike):
    def __init__(self, name, price, maxSpeed, batteryTime):
        super().__init__(name, price, maxSpeed)
        self.batteryTime = batteryTime

    # setters
    def set_batteryTime(self, batteryTime):
        self.batteryTime = batteryTime

    # getters
    def get_batteryTime(self):
        return self.batteryTime


class NormalBike(Bike):
    def __init__(self, name, price, maxSpeed, numOfWheels):
        super().__init__(name, price, maxSpeed)
        self.numOfWheels = numOfWheels

    # setters
    def set_numOfWheels(self, numOfWheels):
        self.numOfWheels = numOfWheels

    # getters
    def get_numOfWheels(self):
        return self.numOfWheels


# main rental class
class MainRentalBike:
    def __init__(self):
        self.listOfBikes = []
        self.listOfRentals = []
        pass

    # setters
    def set_listOfBikes(self, bikeObject):
        self.listOfBikes.append(bikeObject)

    def set_listOfRentals(self, rentalBikeObject):
        self.listOfRentals.append(rentalBikeObject)

    # getters
    def get_listOfBikes(self):
        return self.listOfBikes

    def get_listOfRentals(self):
        return self.listOfRentals

    # methods
    # check age, check bikes num ,
    def requestBike(self, customerObject, numOfBikes):
        # check if age > 6
        if customerObject.get_age() > 6:
            pass
        # check if available bikes > numOfBikes
        if len(self.listOfBikes) > numOfBikes:
            pass

        else:
            print("you are underage")


if __name__ == '__main__':
    # MainRentalBike
    system = MainRentalBike()  # create an object
