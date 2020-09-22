t1a = int(input())
t1b = int(input())
t2a = int(input())
t2b = int(input())

if (t1a - 1 == t2a or t1a + 1 == t2a or t1a == t2a):
    if (t1b - 1 == t2b or t1b + 1 == t2b or t1b == t2b):
        print("YES")
    else:
        print("NO")
else:
    print("NO")
