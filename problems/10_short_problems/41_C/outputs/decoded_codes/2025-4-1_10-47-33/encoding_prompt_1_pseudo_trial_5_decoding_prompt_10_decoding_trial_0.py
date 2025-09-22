def process_input_string():
    # Step 1: Read input
    input_string = input()
    
    # Step 2: Replace keywords
    input_string = input_string.replace('dot', '.').replace('at', '@')
    
    # Step 3: Handle special case for initial character
    if input_string.startswith('.'):
        input_string = 'dot' + input_string[1:]
    
    # Step 4: Initialize variables
    at_count = 0
    result_list = []
    
    # Step 5: Handle special case for email format
    if input_string.startswith('@'):
        result_list.append('at')
        at_count += 1
    
    # Step 6: Process each character
    for current_char in input_string:
        if current_char == '@':
            if at_count > 0:
                result_list.append('at')  # Another '@' found
            else:
                result_list.append('@')  # First '@' found
            at_count += 1
        else:
            result_list.append(current_char)
    
    # Step 7: Combine results
    output_string = ''.join(result_list)
    
    # Step 8: Handle ending special case
    if output_string.endswith('.'):
        output_string = output_string[:-1] + 'dot'
    
    # Step 9: Output result
    print(output_string)

# Call the function to execute
process_input_string()
