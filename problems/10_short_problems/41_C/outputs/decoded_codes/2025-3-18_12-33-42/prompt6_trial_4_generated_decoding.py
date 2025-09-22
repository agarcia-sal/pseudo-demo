# Function to transform the input as described in the pseudocode
def transform_input():
    # Read input from standard input and remove leading/trailing whitespace
    user_input = input().strip()
    
    # Replace occurrences of 'dot' with '.' and 'at' with '@' in the input string
    user_input = user_input.replace('dot', '.')
    user_input = user_input.replace('at', '@')
    
    # If the first character is '.', prepend 'dot' to the string
    if user_input[0] == '.':
        user_input = 'dot' + user_input[1:]

    # Initialize variables
    counter = 0
    transformed_characters = []
    
    # Check if the first character is '@'
    if user_input[0] == '@':
        user_input = 'at' + user_input[1:]

    # Loop through each character in the modified input string
    for character in user_input:
        if character == '@':
            # If '@' has already been added once, add 'at' instead
            if counter > 0:
                transformed_characters.append('at')
                counter = 1
            else:
                transformed_characters.append('@')
                counter = 1
        else:
            # Add any non-'@' character to the list
            transformed_characters.append(character)

    # Join the list of characters back into a single string
    final_output = ''.join(transformed_characters)

    # If the last character of the output string is '.', replace it with 'dot'
    if final_output[-1] == '.':
        final_output = final_output[:-1] + 'dot'

    # Print the final transformed string
    print(final_output)

# Call the function to execute the transformation
transform_input()
