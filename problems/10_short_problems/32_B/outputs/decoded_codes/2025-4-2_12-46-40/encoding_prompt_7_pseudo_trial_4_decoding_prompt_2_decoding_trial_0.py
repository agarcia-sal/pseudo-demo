def translate_dots_and_dashes(inputString):
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

# Read input from standard input
inputString = input()
result = translate_dots_and_dashes(inputString)
print(result)
