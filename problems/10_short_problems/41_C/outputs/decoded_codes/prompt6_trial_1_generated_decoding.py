def process_input():
    # Read input string from standard input
    user_input = input()
    
    # Replace occurrences of 'dot' with '.' and 'at' with '@'
    user_input = user_input.replace('dot', '.')
    user_input = user_input.replace('at', '@')
    
    # If the string starts with '.', prepend 'dot' to the string
    if user_input.startswith('.'):
        user_input = 'dot' + user_input[1:]
    
    # Initialize a count for consecutive '@' symbols
    consecutive_at_count = 0
    # Initialize a list to hold characters for the final output
    processed_characters = []
    
    # If the string starts with '@', prepend 'at' to the string
    if user_input.startswith('@'):
        user_input = 'at' + user_input[1:]
    
    # Iterate through each character in the processed input
    for character in user_input:
        if character == '@':
            # If we already have an '@' in the list, append 'at' instead
            if consecutive_at_count > 0:
                processed_characters.append('at')
                consecutive_at_count = 1
            else:
                processed_characters.append('@')
                consecutive_at_count = 1
        else:
            # If the character is not '@', just add it to the list
            processed_characters.append(character)
    
    # Join the characters in the list into a single string
    final_output = ''.join(processed_characters)

    # If the final string ends with '.', replace it with 'dot'
    if final_output.endswith('.'):
        final_output = final_output[:-1] + 'dot'
    
    # Print the final output string
    print(final_output)

# Call the function to process input
process_input()
