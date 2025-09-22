def process_input_string():
    # Read input from standard input and remove any leading/trailing whitespace
    input_string = input().strip()
    
    # Replace specific substrings in input_string with designated characters
    input_string = input_string.replace('dot', '.')
    input_string = input_string.replace('at', '@')

    # Check if the first character is a dot and prepend 'dot' if true
    if input_string and input_string[0] == '.':
        input_string = 'dot' + input_string[1:]

    # Initialize variables for processing
    count_at_symbol = 0
    character_list = []
    
    # Check if the first character is an at symbol and modify input_string if true
    if input_string and input_string[0] == '@':
        input_string = 'at' + input_string[1:]

    # Process each character in input_string
    for character in input_string:
        if character == '@':
            if count_at_symbol > 0:
                # If this is not the first '@', append 'at' to character_list
                character_list.append('at')
            else:
                # If this is the first '@', append '@' to character_list
                character_list.append('@')
                count_at_symbol += 1
        else:
            # Append non-@ characters to character_list
            character_list.append(character)

    # Join the processed characters into a single string
    processed_string = ''.join(character_list)

    # Check if the last character of processed_string is a dot
    if processed_string and processed_string[-1] == '.':
        # Replace the last dot with 'dot'
        processed_string = processed_string[:-1] + 'dot'

    # Output the final processed string
    print(processed_string)

# Run the function to process input
process_input_string()
