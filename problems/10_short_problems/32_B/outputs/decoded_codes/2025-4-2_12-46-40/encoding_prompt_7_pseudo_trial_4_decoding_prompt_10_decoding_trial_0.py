def translate_dots_and_dashes(input_string):
    index = 0
    answer = ""

    while index < len(input_string):
        if input_string[index] == '.':
            answer += '0'
            index += 1
        elif index + 1 < len(input_string) and input_string[index + 1] == '.':
            answer += '1'
            index += 2
        else:
            answer += '2'
            index += 2

    return answer

# Read input from standard input
input_string = input()
result = translate_dots_and_dashes(input_string)
print(result)


assert translate_dots_and_dashes("") == ""  # Empty input
assert translate_dots_and_dashes(".") == "0"  # Single dot
assert translate_dots_and_dashes("..") == "1"  # Two dots
assert translate_dots_and_dashes("...") == "00"  # Three dots
assert translate_dots_and_dashes(".-") == "2"  # Dot and dash
assert translate_dots_and_dashes("....") == "10"  # Four dots
assert translate_dots_and_dashes(".-.") == "2"  # Dot-dash-dot
