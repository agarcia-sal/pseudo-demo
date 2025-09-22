# Function to translate characters in input string into numeric representation
def translate_input():
    # Read input and strip extra spaces
    input_string = input().strip()
    
    # Initialize variables
    index = 0  # To track current position in the input string
    output_string = ""  # To accumulate the result
    
    # Process input until the end of the string
    while index < len(input_string):
        # If current character is a dot (.)
        if input_string[index] == '.':
            output_string += '0'  # Append '0' to output
            index += 1  # Move to next character
        # Else if the next character is also a dot (.)
        elif index + 1 < len(input_string) and input_string[index + 1] == '.':
            output_string += '1'  # Append '1' to output
            index += 2  # Skip to the character after next
        else:  # No dots found in the above conditions
            output_string += '2'  # Append '2' to output
            index += 2  # Skip to the character after next

    # Output the final translated string
    print(output_string)

# Call the function to execute
translate_input()
