# This function processes an input string by replacing certain words and characters 
# and handles special cases for the characters '.' and '@'.
def process_input():
    # Read input from standard input and remove any surrounding whitespace
    raw_input = input().strip()
    
    # Replace occurrences of 'dot' with '.' in the input
    raw_input = raw_input.replace('dot', '.')
    
    # Replace occurrences of 'at' with '@' in the input
    raw_input = raw_input.replace('at', '@')
    
    # Check if the first character is '.', if so, prepend 'dot' to the string
    if raw_input and raw_input[0] == '.':
        raw_input = 'dot' + raw_input[1:]
    
    # Initialize a variable to count occurrences of '@' in the processed string
    at_counter = 0
    # Initialize a list to hold characters for the final output
    output_list = []
    
    # Check if the first character is '@', if so, prepend 'at' to the string
    if raw_input and raw_input[0] == '@':
        raw_input = 'at' + raw_input[1:]
    
    # Iterate through each character in the processed string
    for character in raw_input:
        # Check if the character is '@'
        if character == '@':
            # If we've already added one '@', add 'at' to the list,
            if at_counter > 0:
                output_list.append('at')
                at_counter = 1
            else:
                output_list.append('@')
                at_counter = 1
        else:
            # If the character is not '@', simply add it to the output list
            output_list.append(character)
    
    # Combine the list of characters into a single string
    final_output = ''.join(output_list)
    
    # If the last character of the final output is '.', replace it with 'dot'
    if final_output and final_output[-1] == '.':
        final_output = final_output[:-1] + 'dot'
    
    # Print the resulting processed string
    print(final_output)

# You may want to test the function with different inputs.
# For example:
# process_input()
