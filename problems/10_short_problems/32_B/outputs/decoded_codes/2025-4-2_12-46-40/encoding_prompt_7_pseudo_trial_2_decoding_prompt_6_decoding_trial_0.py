def translate_symbol_string(input_string):
    # Initialize index to traverse the input string
    index = 0
    # Initialize an empty result string
    result_string = ""

    # Continue looping until the index reaches the end of the input string
    while index < len(input_string):
        if input_string[index] == '.':
            # Append '0' to result_string if current character is '.'
            result_string += '0'
            # Move to the next character
            index += 1
        elif index + 1 < len(input_string) and input_string[index + 1] == '.':
            # Append '1' to result_string if the next character is '.'
            result_string += '1'
            # Move index ahead by 2
            index += 2
        else:
            # Append '2' to result_string if neither condition is met
            result_string += '2'
            # Move index ahead by 2
            index += 2

    # Return the constructed result string
    return result_string

# Read input from standard input
input_string = input()

# Call the translate function and store the result
result = translate_symbol_string(input_string)

# Print the resulting translated string
print(result)
