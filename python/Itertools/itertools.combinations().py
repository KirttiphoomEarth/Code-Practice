from itertools import combinations
# inp = input().split(' ')

# string, num = inp[0], int(inp[1])
# ans = sorted(list(combinations(string, num)))
# print(ans)
# [print(x) for x in sorted(string)]
# for i in ans:
#     x = ''.join(i)
#     print(x)
S, N = input().split()

for i in range(1, int(N)+1):
    for j in combinations(sorted(S), i):
        print(''.join(j))