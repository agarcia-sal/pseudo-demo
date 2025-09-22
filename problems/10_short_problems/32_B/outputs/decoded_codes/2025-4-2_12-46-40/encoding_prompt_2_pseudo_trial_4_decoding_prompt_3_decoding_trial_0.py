def transform_string():
    # Step 1: Read a single line input and trim whitespace
    input_string = input().strip()
    
    # Step 2: Initialize variables
    current_index = 0
    output_string = ""
    
    # Step 3: Process each character in the input string
    while current_index < len(input_string):
        # Check if the current character is a dot
        if input_string[current_index] == '.':
            output_string += '0'  # Append '0' if current character is a dot
            current_index += 1     # Move to the next character
        else:
            # Check the next character if exists
            if current_index + 1 < len(input_string) and input_string[current_index + 1] == '.':
                output_string += '1'  # Append '1' if the next character is a dot
                current_index += 2     # Move to the character after the next
            else:
                output_string += '2'  # Append '2' if the next character is not a dot
                current_index += 2     # Move to the character after the next
    
    # Step 4: Output the transformed string
    print(output_string)

# To execute the function
transform_string()
