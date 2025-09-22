def convert_input_to_output():
    # Get the user's input, stripping unnecessary spaces
    input_string = input().strip()
    
    # Initialize variables
    index = 0
    result = ""
    
    # Loop through the input string until the end is reached
    while index < len(input_string):
        # Check if the current character is a dot
        if input_string[index] == '.':
            result += '0'  # Append '0' to the result
            index += 1  # Increment index by 1
        else:
            # Check the next character after the current one
            if index + 1 < len(input_string) and input_string[index + 1] == '.':
                result += '1'  # Append '1' to the result
                index += 2  # Increment index by 2
            else:
                result += '2'  # Append '2' to the result
                index += 2  # Increment index by 2
                
    # Output the resulting string
    print(result)

# Call the function to execute the program
convert_input_to_output()
