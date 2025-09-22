# Function to process user input and modify it
def process_user_input():
    # Read input from standard input
    userInput = input().strip()  # Remove whitespace from userInput
    
    # Replace 'dot' with '.' and 'at' with '@'
    userInput = userInput.replace('dot', '.').replace('at', '@')
    
    # Ensure input does not start with a '.'
    if userInput.startswith('.'):
        userInput = 'dot' + userInput[1:]
    
    # Initialize variables
    occurrence_counter = 0
    modified_characters = []
    
    # Ensure input does not start with an '@'
    if userInput.startswith('@'):
        userInput = 'at' + userInput[2:]
    
    # Process each character in the userInput
    for character in userInput:
        if character == '@':
            if occurrence_counter > 0:
                modified_characters.append('at')
                occurrence_counter = 1
            else:
                modified_characters.append('@')
                occurrence_counter = 1
        else:
            modified_characters.append(character)
    
    # Join modified characters into a single string
    modified_output = ''.join(modified_characters)
    
    # Ensure output does not end with a '.'
    if modified_output.endswith('.'):
        modified_output = modified_output[:-1] + 'dot'
    
    # Print the final modified output
    print(modified_output)

# Call the function to process the input
process_user_input()
