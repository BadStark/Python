n, m, k = int(input()), int(input()), int(input())
sum = n * m
if k % (sum // n) == 0 and k < sum or k % (sum // m) == 0 and k < sum:
    print("YES")
else:
    print("NO")
