# Function to transform input string according to the specified rules
def transform_input_string():
    # Read input from the user and remove leading or trailing whitespace
    input_string = input().strip()
    
    # Initialize an index variable to track the current position within the string
    index = 0
    
    # Initialize an empty string to build the resulting output
    output_string = ""
    
    # Loop while the current index is less than the length of the input string
    while index < len(input_string):
        # Check if the current character is a dot
        if input_string[index] == '.':
            # Append '0' to the output string
            output_string += '0'
            # Move to the next character
            index += 1
        # Check if the next character is a dot (only if the current character was not a dot)
        elif index + 1 < len(input_string) and input_string[index + 1] == '.':
            # Append '1' to the output string
            output_string += '1'
            # Skip the next character
            index += 2
        # If neither of the above conditions are met, it must be a '00'
        else:
            # Append '2' to the output string
            output_string += '2'
            # Skip the next character
            index += 2
    
    # Output the final result
    print(output_string)

# Call the function to execute the transformation
transform_input_string()
