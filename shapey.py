from abc import ABC, abstractmethod
 
class Shape(ABC):
	@abstractmethod
	def area(self):
		pass

	@abstractmethod
	def perimeter(self):
		pass

	@abstractmethod
	def volume(self):
		pass
	
class Circle(Shape):
	def __init__(self, radius):
		self.radius = radius
		
	def perimeter(self):
		return 2 * 3.14 * self.radius
	
	def area(self):
		return 3.14 * self.radius ** 2
	
	def volume(self):
		return 4*3.14*self.radius**3/3
	
class Rectangle(Shape):
	def __init__(self, width, length, height):
		self.width = width
		self.length = length
		self.height = height
	
	def perimeter(self):
		return 2 * (self.width + self.length)
	
	def area(self):
		return self.width * self.length
	
	def volume(self):
		return self.width *self.length *self.height
	
class Square(Shape):
	def __init__(self, width):
		self.width=width

	def perimeter(self):
		return self.width*4
	
	def area(self):
		return self.width*self.width
	
	def volume(self):
		return self.width*self.width*self.width
		

	
circle = Circle(5) 
rectangle = Rectangle(4, 6, 5)
square = Square(2)

print("Circle Perimeter:", circle.perimeter()) 
print('Circle Volume: ', circle.volume())
print("Rectangle Perimeter:", rectangle.perimeter()) 
print("Rectangle Area: ", rectangle.area())
print("Square Area: ", square.area())
print("Square Perimeter: ", square.perimeter())
print("Cube Volume: ", square.volume())
