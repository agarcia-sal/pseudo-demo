def convert_input_to_output():
    # Get user input and remove any extra spaces
    input_string = input().strip()
    index = 0
    result = ""
    
    # Loop through the input string until the end is reached
    while index < len(input_string):
        # Check if the current character is a dot
        if input_string[index] == '.':
            result += '0'  # Append '0' to result for a dot
            index += 1     # Move to the next character
        else:
            # Check the next character after the current one
            if index + 1 < len(input_string) and input_string[index + 1] == '.':
                result += '1'  # Append '1' to result for a character followed by a dot
                index += 2     # Move past the two characters
            else:
                result += '2'  # Append '2' to result for a character not followed by a dot
                index += 2     # Move past the two characters
                
    # Output the resulting string
    print(result)

# Call the function to execute the program
convert_input_to_output()
