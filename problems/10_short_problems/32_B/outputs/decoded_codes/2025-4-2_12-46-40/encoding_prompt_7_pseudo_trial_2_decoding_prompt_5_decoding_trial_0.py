def translate_symbol_string(input_string):
    index = 0  # Initialize the index to track the position in the input string
    result_string = ""  # Initialize an empty string to store the result

    # Loop through the input string using the index
    while index < len(input_string):
        if input_string[index] == '.':
            result_string += '0'  # Append '0' if the current character is '.'
            index += 1  # Move to the next character
        elif index + 1 < len(input_string) and input_string[index + 1] == '.':
            result_string += '1'  # Append '1' if the next character is '.'
            index += 2  # Move past both characters
        else:
            result_string += '2'  # Append '2' for any other character pattern
            index += 2  # Move past both characters

    return result_string  # Return the final result string

# Read input from the standard input stream
input_string = input()  # Get input from user

# Call the translate function and print the result
result = translate_symbol_string(input_string)
print(result)  # Output the translated result
