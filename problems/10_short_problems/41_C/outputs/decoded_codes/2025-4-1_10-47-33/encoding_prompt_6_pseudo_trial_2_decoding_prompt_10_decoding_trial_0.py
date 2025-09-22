def main():
    # Read a line of input and remove any leading/trailing whitespace
    input_string = input().strip()

    # Replace 'dot' with '.' and 'at' with '@' in the input string
    input_string = input_string.replace('dot', '.')
    input_string = input_string.replace('at', '@')

    # If the first character is '.', prepend 'dot' to the string
    if input_string.startswith('.'):
        input_string = 'dot' + input_string[1:]

    # Initialize a counter for occurrences of '@' and an empty list to hold the result
    at_symbol_counter = 0
    result_list = []

    # If the first character is '@', prepend 'at' to the string
    if input_string.startswith('@'):
        input_string = 'at' + input_string[1:]

    # Iterate through each character in the modified input string
    for character in input_string:
        if character == '@':
            # If another '@' has already been processed
            if at_symbol_counter > 0:
                # Append 'at' to the result list
                result_list.append('at')
                # Update the counter
                at_symbol_counter = 1 
            else:
                # Append '@' to the result list
                result_list.append('@')
                # Update the counter
                at_symbol_counter = 1
        else:
            # Append the current character to the result list
            result_list.append(character)

    # Join the list into a single string
    result_string = ''.join(result_list)

    # If the last character is '.', replace it with 'dot'
    if result_string.endswith('.'):
        result_string = result_string[:-1] + 'dot'

    # Print the final result string
    print(result_string)

# Entry point for the program
if __name__ == "__main__":
    main()
