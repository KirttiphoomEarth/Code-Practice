if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    s1, s2, s3 = student_marks[query_name]
    print("{:.2f}".format((s1 + s2 + s3)/3))