def convert_input_to_binary_string():
    # Read string input from the user
    input_string = input()
    
    # Initialize index for traversing the input string
    index = 0
    
    # Initialize the result string to store the output
    result_string = ""
    
    # Loop through the input string until the end
    while index < len(input_string):
        # If the current character is a '.', append '0' to the result
        if input_string[index] == '.':
            result_string += '0'
            index += 1  # Move to the next character
        # If the next character is also '.', append '1' to the result
        elif index + 1 < len(input_string) and input_string[index + 1] == '.':
            result_string += '1'
            index += 2  # Move past this and the next character
        else:
            # Otherwise, append '2' to the result
            result_string += '2'
            index += 2  # Move past this and the next character
    
    # Print the resulting binary-like string
    print(result_string)

# Example usage (uncomment for direct testing):
# convert_input_to_binary_string()
