def main():
    # Read input from standard input and remove leading/trailing whitespace
    input_string = input().strip()
    
    # Replace occurrences of 'dot' with '.' and 'at' with '@'
    modified_string = input_string.replace('dot', '.').replace('at', '@')

    # If the first character is '.', prepend 'dot'
    if modified_string.startswith('.'):
        modified_string = 'dot' + modified_string[1:]

    # Initialize counter for '@' symbols and a list for characters
    at_counter = 0
    char_list = []
    
    # If the first character is '@', prepend 'at'
    if modified_string.startswith('@'):
        modified_string = 'at' + modified_string[1:]

    # Iterate through each character in the modified string
    for char in modified_string:
        if char == '@':
            # Check if there is already an '@' in the list
            if at_counter > 0:
                char_list.append('at')
            else:
                char_list.append('@')
                at_counter = 1  # Set counter to indicate '@' has been added
        else:
            char_list.append(char)

    # Convert the list back to a string
    final_string = ''.join(char_list)

    # If the last character is '.', replace it with 'dot'
    if final_string.endswith('.'):
        final_string = final_string[:-1] + 'dot'

    # Output the final result
    print(final_string)

# Entry point for the program:
if __name__ == "__main__":
    main()
