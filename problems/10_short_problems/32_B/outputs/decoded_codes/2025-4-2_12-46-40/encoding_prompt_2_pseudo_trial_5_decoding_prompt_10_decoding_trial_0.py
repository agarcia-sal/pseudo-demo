def process_input_string():
    # Step 2: Read input from the user and remove any leading/trailing whitespace
    input_string = input().strip()
    
    # Step 3: Initialize variables
    index = 0
    output_string = ""
    
    # Step 4: Process input
    while index < len(input_string):
        # Check if the current character is a period
        if input_string[index] == '.':
            output_string += '0'  # Append '0' for '.'
            index += 1  # Move to the next character
        # Check if the next character exists and is a period
        elif index + 1 < len(input_string) and input_string[index + 1] == '.':
            output_string += '1'  # Append '1' for current '.' and next '.'
            index += 2  # Skip both characters
        else:
            output_string += '2'  # Append '2' for other characters
            index += 2  # Skip both characters (current and next)
    
    # Step 5: Output the result
    print(output_string)

# Step 6: End Program
if __name__ == "__main__":
    process_input_string()
