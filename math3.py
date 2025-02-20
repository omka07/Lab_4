import math as m

def area(s,l):
    apot = l/(2*m.tan(m.pi/s))
    return (s*l*apot)/2

sides = int(input("Input number of sides: "))
length = int(input("Input the length of a side: "))
result = int(area(sides, length))

print(f"The area of the polygon is: {result}")

