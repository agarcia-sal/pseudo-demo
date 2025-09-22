def convert_dots(input_string):
    # Trim the input string of any leading or trailing whitespace
    input_string = input_string.strip()
    
    # Initialize index variable and an empty result string
    index = 0
    result_string = ''

    # Loop through the characters in the input string
    while index < len(input_string):
        # Check if the current character is a dot
        if input_string[index] == '.':
            # Append '0' to the result string
            result_string += '0'
            index += 1
            
        # Check if the next character exists and is a dot
        elif index + 1 < len(input_string) and input_string[index + 1] == '.':
            # Append '1' to the result string
            result_string += '1'
            index += 2
            
        else:
            # If the next character is not a dot, append '2' to the result string
            result_string += '2'
            index += 2
            
    # Print the final result string
    print(result_string)

# Accept input from the user
user_input = input()  # Get user input here
convert_dots(user_input)
