import math as m

def radians(a):
    p=m.pi
    x = a*(p/180)
    print(f"Output radian: {x}")
deg=int(input("Input degree: "))
radians(deg)
