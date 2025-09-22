def convert_input_to_output():
    # Read input from the user and strip any unnecessary spaces
    user_input = input().strip()
    
    # Initialize index for iterating through the input and an empty result string
    index = 0
    result = ""
    
    # Loop through the input string until the end is reached
    while index < len(user_input):
        # Check if the current character is a dot
        if user_input[index] == '.':
            result += '0'  # Append '0' to the result
            index += 1  # Move to the next character
        else:
            # Check the next character after the current one
            if index + 1 < len(user_input) and user_input[index + 1] == '.':
                result += '1'  # Append '1' to the result
                index += 2  # Move past the current and next character
            else:
                result += '2'  # Append '2' to the result
                index += 2  # Move past the current and next character
    
    # Output the resulting string
    print(result)

# Call the function to execute the program
convert_input_to_output()
