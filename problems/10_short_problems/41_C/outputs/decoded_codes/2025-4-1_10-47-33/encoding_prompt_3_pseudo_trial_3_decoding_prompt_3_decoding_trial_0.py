def main():
    # Read input from the user and remove surrounding whitespace
    user_input = input().strip()

    # Replace all occurrences of 'dot' with '.' in the input
    user_input = user_input.replace('dot', '.')

    # Replace all occurrences of 'at' with '@' in the input
    user_input = user_input.replace('at', '@')

    # If the first character is a '.', prepend 'dot' to the input
    if user_input and user_input[0] == '.':
        user_input = 'dot' + user_input[1:]

    # Initialize a counter for '@' occurrences
    counter = 0
    modified_list = []
    
    # If the first character is an '@', prepend 'at' to the input
    if user_input and user_input[0] == '@':
        user_input = 'at' + user_input[1:]

    # Iterate over each character in modified user_input
    for character in user_input:
        if character == '@':
            # If this is not the first occurrence of '@'
            if counter > 0:
                modified_list.append('at')
            modified_list.append('@')
            counter += 1
        else:
            # If the character is not '@', just add it to the list
            modified_list.append(character)

    # Join all parts in modified_list back into a single string
    final_output = ''.join(modified_list)

    # If the last character of final_output is a '.', replace it with 'dot'
    if final_output and final_output[-1] == '.':
        final_output = final_output[:-1] + 'dot'

    # Output the final result
    print(final_output)

# Call the main function to execute the code
if __name__ == "__main__":
    main()
