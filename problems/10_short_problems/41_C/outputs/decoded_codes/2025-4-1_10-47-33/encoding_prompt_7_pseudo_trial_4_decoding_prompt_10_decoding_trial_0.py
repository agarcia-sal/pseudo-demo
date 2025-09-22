def process_input_address():
    # Read input string from standard input and remove leading/trailing whitespace
    input_address = input().strip()

    # Replace occurrences of specific words with symbols
    input_address = input_address.replace('dot', '.')
    input_address = input_address.replace('at', '@')

    # Ensure the address starts with a valid prefix if it begins with a dot
    if input_address.startswith('.'):
        input_address = 'dot' + input_address[1:]

    # Initialize a counter for occurrences of '@' and a list for building the output
    occurrence_counter = 0
    output_list = []

    # Process the input address
    # If the address starts with '@', prefix it with 'at'
    if input_address.startswith('@'):
        output_list.append('at')
        input_address = input_address[1:]

    # Loop through each character in the processed input address
    for character in input_address:
        if character == '@':
            if occurrence_counter > 0:
                output_list.append('at')
            else:
                output_list.append('@')
            occurrence_counter += 1
        else:
            output_list.append(character)

    # Join the list of characters into a single string
    final_address = ''.join(output_list)

    # If the final character of the address is '.', replace it with 'dot'
    if final_address.endswith('.'):
        final_address = final_address[:-1] + 'dot'

    # Output the final processed address
    print(final_address)

# To call the function:
# process_input_address()
