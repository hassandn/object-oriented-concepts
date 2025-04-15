class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled
    
    def describe(self):
        print(f"It is a {self.color} shape and {'filled' if self.is_filled else 'not filled'}")


class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled) 
        self.radius = radius
        
    def describe(self):
        print(f"the area of the circle is {3.14 * self.radius ** 2}")
        super().describe()


class Square(Shape):
    def __init__(self, color, is_filled, width): 
        super().__init__(color, is_filled) 
        self.width = width 


class Triangle(Shape):
    def __init__(self, color, is_filled, radius, height):
        super().__init__(color, is_filled) 
        self.radius = radius
        self.height = height
        
circle = Circle(color="red", is_filled=True, radius=5)
triangle = Triangle(color="blue", is_filled=False, radius=3, height=4)
square = Square(color="green", is_filled=True, width=10)
print(circle.color)
print(circle.is_filled)
print(circle.radius)

square.describe()
triangle.describe()
circle.describe()

