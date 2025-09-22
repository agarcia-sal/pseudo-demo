def transform_sequence():
    # Step 1: Input
    input_string = input().strip()  # Read and trim whitespace from input
    
    # Step 2: Initialization
    current_index = 0
    output_string = ""
    
    # Step 3: Process Loop
    while current_index < len(input_string):
        if input_string[current_index] == '.':
            output_string += '0'  # Append '0' for '.'
            current_index += 1  # Move to the next character
        else:
            # Check the next character if current is not '.'
            if current_index + 1 < len(input_string) and input_string[current_index + 1] == '.':
                output_string += '1'  # Append '1' for current char followed by '.'
                current_index += 2  # Move to the character after the next
            else:
                output_string += '2'  # Append '2' if next character is not '.'
                current_index += 2  # Move to the character after the next
    
    # Step 4: Output
    print(output_string)  # Print the final output string

# Call the function to execute
transform_sequence()
