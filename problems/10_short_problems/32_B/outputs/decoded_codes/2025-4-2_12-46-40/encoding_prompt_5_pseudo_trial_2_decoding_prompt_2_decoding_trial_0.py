def convert_symbols_to_numbers():
    # Step 1: Read input from the user
    sequence_of_characters = input()
    
    # Step 2: Initialize an index and an empty result string
    current_index = 0
    result_string = ''
    
    # Step 3: Process the input sequence until the end
    while current_index < len(sequence_of_characters):
        # Step 4: Check the current character
        if sequence_of_characters[current_index] == '.':
            # If it's a dot, convert to '0'
            result_string += '0'
            current_index += 1
        elif current_index + 1 < len(sequence_of_characters) and sequence_of_characters[current_index + 1] == '.':
            # If the next character is a dot, convert to '1'
            result_string += '1'
            current_index += 2
        else:
            # If neither is a dot, convert to '2'
            result_string += '2'
            current_index += 2
    
    # Step 5: Output the result
    print(result_string)

# Call the function to execute
convert_symbols_to_numbers()
