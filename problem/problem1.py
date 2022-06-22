def solution(lottos, win_nums):
    answer = []

    numZero = 0
    for i in range(len(lottos)):
        if lottos[i] == 0:
            numZero += 1


    sameNumber = 0
    for i in range(len(win_nums)):
        for j in range(len(lottos)):
            if lottos[j] == win_nums[i]:
                sameNumber += 1
    if numZero == 6:
        answer = [1, 6]

    elif sameNumber == 0 and numZero == 0:
        answer = [6, 6]
    else:
        answer.append(7 - sameNumber - numZero)
        answer.append(7 - sameNumber)

    return answer

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]	))
