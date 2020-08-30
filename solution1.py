n = int(input())
s = n % 60
m = (n // 60) // 100
h = (n // 3600) % 24
print(h, ':', m,m, ':', '0', s, sep = '')
