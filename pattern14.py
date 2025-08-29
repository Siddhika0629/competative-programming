#  Opposite of 9
n = 5
for i in range(1, n+1):
    print("*" * i, end="")
    print(" " * (2*(n-i)), end="")
    print("*" * i)