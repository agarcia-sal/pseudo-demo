def main():
    # Read input from the user and remove surrounding whitespace
    user_input = input().strip()
    
    # Replace occurrences of 'dot' with '.'
    user_input = user_input.replace('dot', '.')
    
    # Replace occurrences of 'at' with '@'
    user_input = user_input.replace('at', '@')
    
    # If the first character is '.', prepend 'dot'
    if user_input and user_input[0] == '.':
        user_input = 'dot' + user_input[1:]
    
    # Initialize a counter for '@' occurrences and an empty list for modified characters
    counter = 0
    modified_list = []
    
    # If the first character is '@', prepend 'at'
    if user_input and user_input[0] == '@':
        user_input = 'at' + user_input[1:]
    
    # Iterate over each character in the modified user_input
    for character in user_input:
        if character == '@':
            # If this is not the first occurrence of '@'
            if counter > 0:
                modified_list.append('at')
                counter = 1
            else:
                modified_list.append('@')
                counter = 1
        else:
            # Just add the character to modified_list
            modified_list.append(character)
    
    # Join the modified list into a single string
    final_output = ''.join(modified_list)
    
    # If the last character of final_output is '.', replace it with 'dot'
    if final_output and final_output[-1] == '.':
        final_output = final_output[:-1] + 'dot'
    
    # Output the final result
    print(final_output)

# Call the main function to execute the code
main()
