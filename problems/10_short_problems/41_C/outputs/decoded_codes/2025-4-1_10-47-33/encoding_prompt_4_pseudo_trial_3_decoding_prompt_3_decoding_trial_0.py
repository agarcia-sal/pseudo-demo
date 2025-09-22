def process_input():
    # Read input from standard input
    user_input = input().strip()  # Removing whitespace from user input
    
    # Replace words with symbols
    user_input = user_input.replace('dot', '.').replace('at', '@')
    
    # Ensure input does not start with a '.'
    if user_input.startswith('.'):
        user_input = 'dot' + user_input[1:]
        
    # Initialize variables
    occurrence_counter = 0
    modified_characters = []
    
    # Ensure input does not start with an '@'
    if user_input.startswith('@'):
        user_input = 'at' + user_input[2:]
    
    # Process each character in the user_input
    for character in user_input:
        if character == '@':
            if occurrence_counter > 0:
                modified_characters.append('at')
                occurrence_counter += 1
            else:
                modified_characters.append('@')
                occurrence_counter += 1
        else:
            modified_characters.append(character)
            occurrence_counter = 0
    
    # Join modified characters into a single string
    modified_output = ''.join(modified_characters)
    
    # Ensure output does not end with a '.'
    if modified_output.endswith('.'):
        modified_output = modified_output[:-1] + 'dot'
    
    # Print the final modified output
    print(modified_output)

# Run the function to get the output
process_input()
