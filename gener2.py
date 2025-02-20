def even(n):
    for i in range(0, n, 2):
        yield i

n = int(input("Enter a number: "))
for num in even(n):
    print(num, end = ", ")