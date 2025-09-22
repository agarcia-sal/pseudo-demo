# Define the main program
def main():
    # Read input from standard input and remove leading/trailing whitespace
    user_input = input().strip()

    # Replace occurrences of 'dot' with '.' and 'at' with '@'
    user_input = user_input.replace('dot', '.').replace('at', '@')

    # If the first character is a dot, prepend 'dot'
    if user_input and user_input[0] == '.':
        user_input = 'dot' + user_input[1:]

    # Initialize a counter for '@' symbols and a list for characters
    at_count = 0
    characters_list = []
    
    # If the first character is an '@', prepend 'at'
    if user_input and user_input[0] == '@':
        user_input = 'at' + user_input[1:]

    # Iterate through each character in the modified input
    for character in user_input:
        if character == '@':
            # Check if there is already an '@' in the list
            if at_count > 0:
                characters_list.append('at')
                at_count = 1
            else:
                characters_list.append('@')
                at_count = 1
        else:
            characters_list.append(character)

    # Convert the list back to a string
    final_output = ''.join(characters_list)

    # If the last character is a dot, replace it with 'dot'
    if final_output and final_output[-1] == '.':
        final_output = final_output[:-1] + 'dot'

    # Output the final result
    print(final_output)

# Call the main function to execute the program
main()
