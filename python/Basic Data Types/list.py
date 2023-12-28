if __name__ == '__main__':
    N = int(input())
    ans = []
    show_ans = []
    for i in range(N):
        commands = input().split()
        if commands[0] == 'insert':
            ans.insert(int(commands[1]), int(commands[2]))
        elif commands[0] == 'print':
            show_ans.append(ans)
        elif commands[0] == 'remove':
            ans.remove(int(commands[1]))
        elif commands[0] == 'append':
            ans.append(int(commands[1]))
        elif commands[0] == 'sort':
            ans.sort()
        elif commands[0] == 'pop':
            ans.pop()
        elif commands[0] == 'reverse':
            ans.reverse()
    [print(x) for x in show_ans]