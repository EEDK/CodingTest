def solution(array, commands):
    answer = []

    for i in range(len(commands)):
        choppedArray = array[commands[i][0] - 1: commands[i][1]]
        choppedArray.sort()
        answer.append(choppedArray[commands[i][2] - 1])

    return answer
