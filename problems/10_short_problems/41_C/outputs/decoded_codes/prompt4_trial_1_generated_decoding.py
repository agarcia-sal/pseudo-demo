def transform_string():
    # Read input string from standard input
    input_string = input()

    # Replace occurrences of 'dot' with '.' and 'at' with '@'
    input_string = input_string.replace('dot', '.').replace('at', '@')

    # If the first character is '.', prepend 'dot'
    if input_string and input_string[0] == '.':
        input_string = 'dot' + input_string[1:]

    # Initialize count and list to store characters
    count = 0
    output_list = []

    # If the first character is '@', prepend 'at'
    if input_string and input_string[0] == '@':
        input_string = 'at' + input_string[1:]

    # Iterate through each character in the input string
    for character in input_string:
        if character == '@':
            # If the count is greater than 0, append 'at' to the output list
            if count > 0:
                output_list.append('at')
                count = 1 
            else:
                # Else, append '@' to the output list
                output_list.append('@')
                count = 1
        else:
            # Append the current character to the output list
            output_list.append(character)

    # Join the output list into a single string
    final_string = ''.join(output_list)

    # If the last character is '.', replace it with 'dot'
    if final_string and final_string[-1] == '.':
        final_string = final_string[:-1] + 'dot'

    # Print the modified string
    print(final_string)

# Run the function to transform a string
transform_string()
