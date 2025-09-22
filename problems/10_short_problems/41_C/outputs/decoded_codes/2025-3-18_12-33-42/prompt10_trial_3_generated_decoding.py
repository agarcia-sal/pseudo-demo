def process_input():
    # Read input
    input_string = input().strip()
    
    # Replace specific terms with symbols
    input_string = input_string.replace("dot", ".").replace("at", "@")
    
    # Initialize count and output list
    count_of_at = 0
    output_list = []
    
    # Check for leading dot and adjust
    if input_string.startswith('.'):
        input_string = "dot" + input_string[1:]

    # Check for leading at and adjust
    if input_string.startswith('@'):
        input_string = "at" + input_string[1:]

    # Process each character in input_string
    for character in input_string:
        if character == '@':
            if count_of_at > 0:
                output_list.append("at")
            else:
                output_list.append("@")
            count_of_at = 1
        else:
            output_list.append(character)
            count_of_at = 0  # Reset after adding a non-'@' character

    # Join the list into a single string
    final_string = ''.join(output_list)
    
    # Check for trailing dot and adjust
    if final_string.endswith('.'):
        final_string = final_string[:-1] + 'dot'
    
    # Output the final result
    print(final_string)

# Call the function to execute the process
process_input()
