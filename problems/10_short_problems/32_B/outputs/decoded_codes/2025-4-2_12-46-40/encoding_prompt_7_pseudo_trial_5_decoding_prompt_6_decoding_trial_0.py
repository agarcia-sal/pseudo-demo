def convert_input_to_binary_string():
    # Read input string from standard input
    input_string = input()
    # Initialize index to track position in the input string
    index = 0
    # Initialize result string to store the output
    result_string = ''

    # Iterate through the input string while index is less than its length
    while index < len(input_string):
        # Check if the current character is a dot '.'
        if input_string[index] == '.':
            result_string += '0'  # Append '0' if current character is '.'
            index += 1  # Move to the next character
        # Check if the next character is also a dot '.'
        elif index + 1 < len(input_string) and input_string[index + 1] == '.':
            result_string += '1'  # Append '1' if the next character is also '.'
            index += 2  # Move the index past both characters
        else:
            result_string += '2'  # Append '2' for any other single character
            index += 2  # Move the index past two characters

    # Print the resulting string
    print(result_string)

# Call the function to execute
convert_input_to_binary_string()
