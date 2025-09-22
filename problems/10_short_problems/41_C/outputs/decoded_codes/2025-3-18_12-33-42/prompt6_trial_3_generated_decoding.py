def main():
    # Read a line of input
    input_string = input()
    
    # Replace the word 'dot' with the character '.'
    input_string = input_string.replace('dot', '.')
    # Replace the word 'at' with the character '@'
    input_string = input_string.replace('at', '@')

    # Verify if the first character is a period (.)
    if input_string[0] == '.':
        # If so, prepend 'dot' before the rest of the string
        input_string = 'dot' + input_string

    count_of_at_symbol = 0  # Variable to count occurrences of '@'
    result_list = []  # List to store the modified characters

    # Check if the first character is an '@' symbol
    if input_string[0] == '@':
        # If so, prepend 'at' before the rest of the string
        input_string = 'at' + input_string

    # Iterate through each character in the input_string
    for character in input_string:
        if character == '@':
            # If an '@' has already been encountered
            if count_of_at_symbol > 0:
                # Append 'at' to the result list if '@' was found before
                result_list.append('at')
            # Append '@' to the result list
            result_list.append('@')
            count_of_at_symbol += 1  # Keep track of '@' cases
        else:
            # Append the current character to the result list
            result_list.append(character)

    # Join all elements in the result_list to form the final string
    combined_string = ''.join(result_list)

    # Check if the last character is a period (.)
    if combined_string[-1] == '.':
        # If so, remove the last character and append 'dot'
        combined_string = combined_string[:-1] + 'dot'

    # Output the final modified string
    print(combined_string)

# Call main function to execute the logic
main()
