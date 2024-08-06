# TODO: Add code here
import matplotlib.pyplot as plt


class Point:
    def __init__(self, x: float, y: float):
        self.x: float = x
        self.y: float = y

class Circle:
    def __init__(self, center: Point, radius: float):
        self.center: Point = center
        self.radius: float = radius

    area = 0
    pi = 3.1416

    def area(self):
        area = pi * (self.radius ** 2)
        return area

    Rad = float(input("Por favor ingrese el radio"))
    Are = area(Rad)
    print("El area del circulo es: ", Are)

    def draw(self) :
        circle = plt.circle((self.center.x, self.center.y), self.radius, color="r")
        plt.gca().add_patch(circle)
        plt.axis("scaled")
        plt.show()

    def __str__(self):
        Circle
        return f"with center at {self.x}, {self.y} and {self.radius}"


class Triangle:
    def __init__(self, point_1:Point, point_2: Point, point_3: Point):
        self.point_1: Point = point_1
        self.point_2: Point = point_2
        self.point_1: Point = point_3

    def area(self):
        area= (base * altura) / 2
        return area

    base= float(input("Ingrese la base del triangulo"))
    altura= float(input("Ingrese la base"))

    def draw(self):
        x = [self.point_1.x, self.point_2.x, self.point_3.x, self.point_1.x]
        y = [self.point_1.y, self.point_2.y, self.point_3.y, self.point_1.y]
        plt.fill(x, y, color='b')
        plt.axis("scaled")
        plt.show()

    def __str__(self):
        Triangle
        return f"with vertices at {self.x1, self.y1}, {self.x2, self.y2} and {self.x3, self.y3}"






