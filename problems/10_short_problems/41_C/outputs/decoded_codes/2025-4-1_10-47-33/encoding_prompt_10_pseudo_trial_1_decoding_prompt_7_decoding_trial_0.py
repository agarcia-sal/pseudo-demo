# Function to process the input string according to specified rules
def process_input():
    # Step 1: Read input
    input_line = input().strip()  # Read input and remove any surrounding whitespace
    input_line = input_line.replace('dot', '.')  # Replace 'dot' with '.'
    input_line = input_line.replace('at', '@')  # Replace 'at' with '@'

    # Handle leading dot
    if input_line.startswith('.'):
        input_line = 'dot' + input_line[1:]  # Change leading '.' to 'dot'

    counter = 0  # Initialize counter
    c = []  # Initialize empty list for characters
    length = 0  # Placeholder for length, not used further

    # Step 3: Handle leading at sign
    if input_line.startswith('@'):
        input_line = 'at' + input_line[1:]  # Change leading '@' to 'at'

    # Step 4: Process each character of the input_line
    for character in input_line:
        if character == '@':
            if counter > 0:
                c.append('at')  # Append 'at' if counter > 0
                counter = 1  # Reset counter
            else:
                c.append('@')  # Append '@' if counter is 0
                counter = 1  # Set counter
        else:
            c.append(character)  # Append the character if it's not '@'

    # Step 5: Join list c into final string
    final_output = ''.join(c)  # Join characters in list c into a single string

    # Step 6: Handle trailing dot
    if final_output.endswith('.'):
        final_output = final_output[:-1] + 'dot'  # Replace trailing '.' with 'dot'

    # Step 7: Output the final result
    print(final_output)  # Print the final output

# Call the function to execute the program
process_input()
