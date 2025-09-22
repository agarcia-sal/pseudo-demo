def translate_symbol_string(input_string):
    # Initialize index to track position in the input string
    index = 0
    # Initialize the result string to build the output
    result_string = ""

    # Process the input string until the end is reached
    while index < len(input_string):
        # Check if the current character is '.'
        if input_string[index] == '.':
            # Append '0' to the result string
            result_string += '0'
            # Move to the next character
            index += 1
        # Check if the next character is also '.'
        elif index + 1 < len(input_string) and input_string[index + 1] == '.':
            # Append '1' to the result string
            result_string += '1'
            # Skip the next character as well
            index += 2
        else:
            # If there is no '.', append '2' and skip the next character
            result_string += '2'
            index += 2

    return result_string

# Read input from the standard input
input_string = input()

# Call the translate function and print the result
result = translate_symbol_string(input_string)
print(result)
