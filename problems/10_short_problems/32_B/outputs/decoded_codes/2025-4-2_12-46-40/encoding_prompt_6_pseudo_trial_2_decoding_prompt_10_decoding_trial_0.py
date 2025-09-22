def process_input_string():
    # Read input string from standard input
    input_string = input().strip()

    # Initialize index and output variable
    index = 0
    output_string = ''

    # Loop through the input string until the end
    while index < len(input_string):
        # Check if the current character is '.'
        if input_string[index] == '.':
            output_string += '0'  # Append '0' to the output
            index += 1  # Move to the next character
        
        # Check for the pattern ".."
        elif index + 1 < len(input_string) and input_string[index + 1] == '.':
            output_string += '1'  # Append '1' to the output
            index += 2  # Move the index forward by two characters

        # Otherwise, the pattern is '.-' or another character
        else:
            output_string += '2'  # Append '2' to the output
            index += 2  # Move the index forward by two characters

    # Output the final result
    print(output_string)

# Call the function
process_input_string()
