#Program to draw a pattern of a mirrored right angle triangle
n = int(input("Enter the number of rows: "))
for i in range(1, n+1):
    print(" " * (n-i) + "*" * i)
for i in range(n-1, 0, -1):
    print(" " * (n-i) + "*" * i)