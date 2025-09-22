def process_input():
    # Step 1: Read input
    input_line = input().strip()
    input_line = input_line.replace('dot', '.').replace('at', '@')

    # Step 2: Handle leading dot
    if input_line.startswith('.'):
        input_line = 'dot' + input_line[1:]

    counter = 0
    processed_chars = []
    
    # Step 3: Handle leading at sign
    if input_line.startswith('@'):
        input_line = 'at' + input_line[1:]

    # Step 4: Process each character of the input_line
    for character in input_line:
        if character == '@':
            if counter > 0:
                processed_chars.append('at')
                counter = 1
            else:
                processed_chars.append('@')
                counter = 1
        else:
            processed_chars.append(character)

    # Step 5: Join list processed_chars into final string
    final_output = ''.join(processed_chars)

    # Step 6: Handle trailing dot
    if final_output.endswith('.'):
        final_output = final_output[:-1] + 'dot'

    # Step 7: Output the final result
    print(final_output)

# Call the function to run the processing
process_input()
