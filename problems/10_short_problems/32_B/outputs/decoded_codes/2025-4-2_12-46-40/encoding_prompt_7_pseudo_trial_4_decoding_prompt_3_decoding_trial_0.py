def translate_dots_and_dashes(input_string):
    index = 0
    answer = ""

    while index < len(input_string):
        if input_string[index] == '.':
            answer += '0'  # A single dot translates to '0'
            index += 1
        elif index + 1 < len(input_string) and input_string[index + 1] == '.':
            answer += '1'  # A dot followed by another dot translates to '1'
            index += 2
        else:
            answer += '2'  # Any other character (dash) translates to '2'
            index += 2

    return answer

# Read input from standard input
input_string = input()
result = translate_dots_and_dashes(input_string)
print(result)
