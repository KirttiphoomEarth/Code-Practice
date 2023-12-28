from itertools import combinations_with_replacement

inp = input().split(' ')

string, num = inp[0], int(inp[1])
ans = list(combinations_with_replacement(sorted(string), num))
[print(f"{''.join(x)}") for x in ans]
