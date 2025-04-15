from car import Car
# this is how we create an object of the class Car
bmw_x3 = Car("BMW X3", 2020, "black", True)
# this is how we access the attributes of the object
print(bmw_x3.model)
print(bmw_x3.year)
print(bmw_x3.color)
print(bmw_x3.for_sale)
# this is how we access methods of the object
bmw_x3.drive()
bmw_x3.stop()
bmw_x3.describe()