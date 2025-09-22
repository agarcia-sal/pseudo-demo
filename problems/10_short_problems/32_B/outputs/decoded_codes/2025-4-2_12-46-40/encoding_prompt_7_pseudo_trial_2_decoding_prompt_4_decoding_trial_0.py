def translate_symbol_string(input_string):
    index = 0
    result_string = ""

    while index < len(input_string):
        if input_string[index] == '.':
            result_string += '0'
            index += 1
        elif index + 1 < len(input_string) and input_string[index + 1] == '.':
            result_string += '1'
            index += 2
        else:
            result_string += '2'
            index += 2

    return result_string

# Read input from the standard input stream
input_data = input()

# Call the translate function and print the result
result = translate_symbol_string(input_data)
print(result)
