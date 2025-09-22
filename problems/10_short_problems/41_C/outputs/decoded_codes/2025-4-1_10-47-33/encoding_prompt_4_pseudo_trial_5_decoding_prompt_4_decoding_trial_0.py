def main():
    # Step 1: Read a line of input and remove leading and trailing spaces
    input_string = input().strip()

    # Step 2: Replace occurrences of 'dot' with '.' and 'at' with '@'
    transformed_string = input_string.replace('dot', '.').replace('at', '@')

    # Step 3: If the first character is '.', prepend 'dot'
    if transformed_string.startswith('.'):
        transformed_string = 'dot' + transformed_string[1:]

    # Step 4: Initialize a counter and a list to hold characters
    counter = 0
    character_list = []

    # Step 5: If the string starts with '@', prepend 'at'
    if transformed_string.startswith('@'):
        transformed_string = 'at' + transformed_string[1:]

    # Step 6: Iterate through each character in the transformed string
    for character in transformed_string:
        if character == '@':
            # If we've already processed an '@', replace it with 'at'
            if counter > 0:
                character_list.append('at')
            else:
                character_list.append('@')
            counter = 1
        else:
            # Add non-special characters to the list
            character_list.append(character)
            counter = 0  # Reset the counter for non-special characters

    # Step 7: Join the characters in the list to form the final string
    final_string = ''.join(character_list)

    # Step 8: If the last character is '.', replace it with 'dot'
    if final_string.endswith('.'):
        final_string = final_string[:-1] + 'dot'

    # Step 9: Print the final transformed string
    print(final_string)

# Call the main function to execute the code
if __name__ == "__main__":
    main()
