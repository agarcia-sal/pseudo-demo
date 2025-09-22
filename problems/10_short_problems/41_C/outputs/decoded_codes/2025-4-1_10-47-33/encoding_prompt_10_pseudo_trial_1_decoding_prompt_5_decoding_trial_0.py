# Function to process the input string as specified in the pseudocode
def process_input_string():
    # Step 1: Read input
    input_line = input().strip()  # Read and strip whitespace
    input_line = input_line.replace('dot', '.')  # Replace 'dot' with '.'
    input_line = input_line.replace('at', '@')    # Replace 'at' with '@'

    # Step 2: Handle leading dot
    if input_line.startswith('.'):
        input_line = 'dot' + input_line[1:]  # Replace leading dot with 'dot'

    # Initialize variables
    counter = 0
    character_list = []  # List to hold processed characters
    length = 0

    # Step 3: Handle leading at sign
    if input_line.startswith('@'):
        input_line = 'at' + input_line[1:]  # Replace leading @ with 'at'

    # Step 4: Process each character of the input_line
    for character in input_line:
        if character == '@':  # Check if character is '@'
            if counter > 0:
                character_list.append('at')  # Append 'at' if counter is more than 0
                counter = 1
            else:
                character_list.append('@')  # Append '@' if counter is 0
                counter = 1
        else:
            character_list.append(character)  # Append current character

    # Step 5: Join the list into a final string
    final_output = ''.join(character_list)  # Join characters into a single string

    # Step 6: Handle trailing dot
    if final_output.endswith('.'):
        final_output = final_output[:-1] + 'dot'  # Replace trailing dot with 'dot'

    # Step 7: Output the final result
    print(final_output)  # Print the processed output

# Call the function to execute the code
process_input_string()
