
import math

def polygon_area(n, s):
    return (n * s ** 2) / (4 * math.tan(math.pi / n))

n = int(input("Enter the number of sides of the polygon: "))
s = int(input("Enter the length of the side of the polygon: "))

print("The area of the polygon is: ", polygon_area(n, s))
#generate a polygon perimeter calculator
def polygon_perimeter(n, s):
    return n * s

n = int(input("Enter the number of sides of the polygon: "))
s = int(input("Enter the length of the side of the polygon: "))

print("The perimeter of the polygon is: ", polygon_perimeter(n, s))

