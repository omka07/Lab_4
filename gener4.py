def squares(a,b):
    for i in range(a,b+1):
        i*=i
        yield i

a = int(input("Enter a first number: "))
b = int(input("Enter a second number: "))

for num in squares(a,b):
    print(num, end=" ")