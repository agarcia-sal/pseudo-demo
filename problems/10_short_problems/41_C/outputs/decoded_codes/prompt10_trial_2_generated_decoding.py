def transform_string():
    # Step 1: Read input and remove whitespace
    input_string = input().strip()

    # Step 2: Replace specific strings
    input_string = input_string.replace('dot', '.').replace('at', '@')

    # Step 3: Check for leading '.' and modify if necessary
    if input_string.startswith('.'):
        input_string = 'dot' + input_string[1:]

    # Step 4: Initialize counters and lists
    counter = 0
    characters_list = []
    
    # Step 5: Check for leading '@' and modify if necessary
    if input_string.startswith('@'):
        input_string = 'at' + input_string[1:]

    # Step 6: Process each character in input_string
    for character in input_string:
        if character == '@':
            if counter > 0:
                characters_list.append('at')
            else:
                characters_list.append('@')
            counter = 1
        else:
            characters_list.append(character)

    # Step 7: Join characters to form the final string
    output_string = ''.join(characters_list)

    # Step 8: Check for trailing '.' and modify if necessary
    if output_string.endswith('.'):
        output_string = output_string[:-1] + 'dot'

    # Step 9: Print the result
    print(output_string)

# To run the function
if __name__ == "__main__":
    transform_string()
