if __name__ == '__main__':
    student = []
    grade_sec_input = set()     #NO dupictae
    ans = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student.append([name, score])
        grade_sec_input.add(score)

grade_sec = sorted(grade_sec_input)[1]

for name,score in student:
    if score == grade_sec:
        ans.append(name)

for x in sorted(ans):
    print(x)

