def divide(n):
    for i in range(0, n):
        if i%3==0 and i%4==0: 
            yield i
        else:
            continue

n = int(input("Enter a number: "))
for num in divide(n):
    print(num, end = ", ")