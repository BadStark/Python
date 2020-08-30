n = int(input())
s = n % 60
m = (n // 60) % 60
h = (n // 3600) % 24
print(h, ':', m // 10, m % 10, ':', s // 10, s % 10, sep='')
