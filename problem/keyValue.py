def solution(participant, completion):

    dict1 = {}
    sum = 0

    for user in participant:
        dict1[hash(user)] = user
        sum += hash(user)

    for comp in completion:
        sum -= hash(comp)

    return dict1[sum]



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(solution(participant=["leo", "kiki", "eden"], completion=["eden", "kiki"]	))
