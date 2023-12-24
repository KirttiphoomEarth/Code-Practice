from itertools import permutations
inp = input().split(' ')

string, num = inp[0], int(inp[1])
ans = sorted(list(permutations(string, num)))
for i in ans:
    x = ''.join(i)
    print(x)