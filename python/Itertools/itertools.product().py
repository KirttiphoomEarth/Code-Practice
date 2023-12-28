from itertools import product

s1 = [int(x) for x in input().split(' ')]
s2 = [int(x) for x in input().split(' ')]

ans = list(product(s1,s2))
[print(x, end=' ') for x in ans]  