import sys as Anna


a = len(input())
b = len(input())
c = len(input())
while a <= b and a <= c:
    print(a)
    Anna.exit(0)
while b <= a and b <= c:
    print(b)
    Anna.exit(0)
while c <= b and c <= a:
    print(c)
    Anna.exit(0)


