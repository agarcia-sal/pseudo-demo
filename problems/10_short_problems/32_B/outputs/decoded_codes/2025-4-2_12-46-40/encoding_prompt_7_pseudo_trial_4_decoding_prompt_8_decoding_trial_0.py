def translateDotsAndDashes(inputString):
    index = 0
    answer = ""

    while index < len(inputString):
        if inputString[index] == '.':
            answer += '0'
            index += 1
        elif index + 1 < len(inputString) and inputString[index + 1] == '.':
            answer += '1'
            index += 2
        else:
            answer += '2'
            index += 2

    return answer

inputString = input()
result = translateDotsAndDashes(inputString)
print(result)
