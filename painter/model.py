# TODO: Add code here
import matplotlib


class Point:
    def __init__(self, x: float, y: float):
        self.x: float = x
        self.y: float = y

class circle:
    def __init__(self, center: Point, radius: float):
        self.center: Point = center
        self.radius: float = radius

area = 0
pi = 3.1416
def areacirculo (radio):
    area= pi * (radio **2)
    return area

Rad = float (input("Por favor ingrese el radio"))
Are= areacirculo(Rad)
print ("El area del circulo es: ",  Are)

def draw():
    circle = matplotlib.circle((self.center.x, self.center.y), self.radius, color="r")
    matplotlib.gca().add_patch(circle)
    matplotlib.axis("scaled")
    matplotlib.show()

