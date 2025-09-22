def transform_string():
    # Read input from the user
    input_string = input()
    
    # Replace occurrences of 'dot' with '.'
    input_string = input_string.replace('dot', '.')
    
    # Replace occurrences of 'at' with '@'
    input_string = input_string.replace('at', '@')

    # Handle special cases for leading symbols
    if input_string.startswith('.'):
        input_string = 'dot' + input_string[1:]
    
    # Initialize a counter for '@' symbols and a list for building the output
    at_counter = 0
    output_list = []

    if input_string.startswith('@'):
        input_string = 'at' + input_string[1:]

    # Iterate through each character in the updated input_string
    for character in input_string:
        if character == '@':
            if at_counter > 0:
                output_list.append('at')  # Replace subsequent '@' with 'at'
                # We do not increment `at_counter` here to indicate another '@'
            else:
                output_list.append('@')
                at_counter += 1  # Mark the first '@' has been added
        else:
            output_list.append(character)
    
    # Join the list of characters into a single string
    final_output = ''.join(output_list)
    
    # Handle the case of the last character being '.'
    if final_output.endswith('.'):
        final_output = final_output[:-1] + 'dot'
    
    # Print the final transformed output
    print(final_output)

# To execute the function
transform_string()
