#Area of a Circle
import math
#radius=float(input("radius of the circle= "))
try:
    radius=float(input("radius of the circle= "))
    area= math.pi*(radius**2)
    print(area)
except:
    print("Recheck your code dummy")