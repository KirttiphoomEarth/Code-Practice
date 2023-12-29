def count_substring(string, sub_string):
    return 1

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    print(string, sub_string)

    count = count_substring(string, sub_string)
    print(count)