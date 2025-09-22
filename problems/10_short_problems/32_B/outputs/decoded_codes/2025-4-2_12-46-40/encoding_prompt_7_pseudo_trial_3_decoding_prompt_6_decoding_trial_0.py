def translate_input_to_output():
    # Read input from standard input and remove any trailing whitespace
    string_input = input().strip()
    
    # Initialize an index to track position in the input string
    index = 0
    # Initialize an empty string to hold the output result
    output_result = ""
    
    # While index is within the bounds of the input string
    while index < len(string_input):
        # If the current character is a dot
        if string_input[index] == '.':
            # Append '0' to the output result
            output_result += '0'
            # Move to the next character
            index += 1
        # Else if the next character is also a dot and index is within bounds
        elif index + 1 < len(string_input) and string_input[index + 1] == '.':
            # Append '1' to the output result
            output_result += '1'
            # Move to the character after the next
            index += 2
        # Otherwise, the next two characters are different from dots
        else:
            # Append '2' to the output result
            output_result += '2'
            # Move to the character after the next
            index += 2
    
    # Output the constructed result string
    print(output_result)

# Call the function to execute
translate_input_to_output()
