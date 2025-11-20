def sum_no(n):
    if n == 0:
        return 0
    return n + sum_no(n - 1)
print(sum_no(5)) #Output: 15