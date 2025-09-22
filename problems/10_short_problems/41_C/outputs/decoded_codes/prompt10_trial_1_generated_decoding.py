def process_input_string():
    # Step 1: Read a line of input and remove whitespace
    input_string = input().strip()

    # Step 2: Replace 'dot' with '.' and 'at' with '@'
    input_string = input_string.replace('dot', '.').replace('at', '@')

    # Step 3: Adjust input string if it starts with '.'
    if input_string.startswith('.'):
        input_string = 'dot' + input_string

    # Step 4: Initialize count and list to build transformed output
    count = 0
    output_characters = []

    # Step 5: Adjust input string if it starts with '@'
    if input_string.startswith('@'):
        input_string = 'at' + input_string

    # Step 6: Process each character in the modified string
    for character in input_string:
        if character == '@':
            if count > 0:
                output_characters.append('at')
                count = 1
            else:
                output_characters.append('@')
                count = 1
        else:
            output_characters.append(character)

    # Step 7: Join the output_characters list into a single string
    result_string = ''.join(output_characters)

    # Step 8: Replace trailing '.' with 'dot' if present
    if result_string.endswith('.'):
        result_string = result_string[:-1] + 'dot'

    # Step 9: Print the final result
    print(result_string)

# Run the function to execute the process
process_input_string()
