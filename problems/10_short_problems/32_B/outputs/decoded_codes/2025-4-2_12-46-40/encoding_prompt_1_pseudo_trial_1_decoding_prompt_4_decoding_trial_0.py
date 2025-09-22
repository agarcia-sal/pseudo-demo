def convert_string_to_numeric_string():
    # Step 2: Read input and strip whitespace
    input_string = input().strip()
    
    # Step 3: Initialize variables
    current_index = 0
    result = ""
    
    # Step 5: Process the input string
    while current_index < len(input_string):
        if input_string[current_index] == '.':
            # Append '0' for single dot
            result += '0'
            current_index += 1
        elif current_index + 1 < len(input_string) and input_string[current_index + 1] == '.':
            # Append '1' for dot followed by another dot
            result += '1'
            current_index += 2
        else:
            # Append '2' for any other character
            result += '2'
            current_index += 2
    
    # Step 6: Output the result
    print(result)

# Entry point to call the conversion function
if __name__ == "__main__":
    convert_string_to_numeric_string()
