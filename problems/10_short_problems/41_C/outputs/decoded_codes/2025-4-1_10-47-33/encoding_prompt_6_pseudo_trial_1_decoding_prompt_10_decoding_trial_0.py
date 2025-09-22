def process_email(input_string):
    # Read input removing any surrounding whitespace
    raw_input = input_string.strip()

    # Replace occurrences of 'dot' with '.'
    raw_input = raw_input.replace('dot', '.')

    # Replace occurrences of 'at' with '@'
    raw_input = raw_input.replace('at', '@')

    # Prepend 'dot' if the first character is '.'
    if raw_input.startswith('.'):
        raw_input = 'dot' + raw_input[1:]

    # Counter for occurrences of '@'
    at_counter = 0
    # List to hold characters for final output
    output_list = []

    # Prepend 'at' if the first character is '@'
    if raw_input.startswith('@'):
        raw_input = 'at' + raw_input[1:]

    # Iterate through each character in the processed string
    for character in raw_input:
        # Check if character is '@'
        if character == '@':
            if at_counter > 0:
                output_list.append('at')  # Add 'at' for additional '@'
            else:
                output_list.append('@')    # First '@'
            at_counter += 1  # Increment the counter
        else:
            output_list.append(character)  # Add non-'@' characters to the list

    # Combine the list of characters into a single string
    final_output = ''.join(output_list)

    # If the last character is '.', replace it with 'dot'
    if final_output.endswith('.'):
        final_output = final_output[:-1] + 'dot'

    # Print the resulting processed string
    print(final_output)

# Example usage:
if __name__ == "__main__":
    user_input = input()
    process_email(user_input)
