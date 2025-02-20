import math as m

def area(h,a,b):
    return h*((a+b)/2)

height = int(input("Height: "))
base_a = int(input("Base, first value: "))
base_b = int(input("Base, second value: "))
output = area(height,base_a,base_b)

print(f"Expected Output: {output}")