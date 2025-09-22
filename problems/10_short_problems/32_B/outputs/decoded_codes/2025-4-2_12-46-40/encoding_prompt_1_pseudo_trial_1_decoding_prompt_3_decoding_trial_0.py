def convert_string_to_numeric():
    # Step 2: Read input and trim whitespace
    input_string = input().strip()  # Store input in input_string
    
    # Step 3: Initialize variables
    current_index = 0  # To track the current position in the input string
    result = ""        # To hold the final numeric string output

    # Step 5: Process the input string
    while current_index < len(input_string):
        if input_string[current_index] == '.':
            # If current character is a dot
            result += '0'      # Append '0' to result
            current_index += 1 # Move to the next character
        elif (current_index + 1 < len(input_string) and 
              input_string[current_index + 1] == '.'):
            # If the next character is also a dot
            result += '1'      # Append '1' to result
            current_index += 2 # Move ahead by 2 characters
        else:
            # For any other character
            result += '2'      # Append '2' to result
            current_index += 2 # Move ahead by 2 characters

    # Step 6: Output the final result
    print(result)

# Call the function to execute the conversion
convert_string_to_numeric()
