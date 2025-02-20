import math as m

def area(b,h):
    return b*h

base = int(input("Length of base: "))
height = int(input("Height of parallelogram: "))
result = float(area(base, height))

print(f"Expected Output: {result}")
