def translate_dots_to_numbers():
    # Read the input string and strip any surrounding whitespace
    input_string = input().strip()
    
    # Initialize index for tracking positions and an empty output string
    index = 0
    output_string = ""
    
    # Process the input string until the end
    while index < len(input_string):
        if input_string[index] == '.':
            # If the current character is a dot, append '0'
            output_string += '0'
            index += 1  # Move to the next character
        elif index + 1 < len(input_string) and input_string[index + 1] == '.':
            # If the next character is also a dot, append '1'
            output_string += '1'
            index += 2  # Skip to the character after the next
        else:
            # If no conditions are met, append '2'
            output_string += '2'
            index += 2  # Skip to the character after the next
    
    # Print the final output string
    print(output_string)

# Call the function to execute
translate_dots_to_numbers()
