def solution(n, lost, reserve):
    student = []
    for i in range(n):
        student.append(1)

    for i in range(len(reserve)):
        student[reserve[i] - 1] = 2

    for i in range(len(lost)):
        student[lost[i] - 1] -= 1

    if student[0] == 0 and student[1] == 2:
        student[0] = 1
        student[1] = 1

    if student[n-1] == 0 and student[n-2] == 2:
        student[n-1] = 1
        student[n-2] = 1

    for i in range(1, len(student)-1):
        if student[i] == 0:
            if student[i - 1] == 2:
                student[i] += 1
                student[i-1] -= 1
            elif student[i + 1] == 2:
                student[i] += 1
                student[i+1] -= 1

    answer = 0
    for j in range(len(student)):
        if student[j] != 0:
            answer += 1

    return answer