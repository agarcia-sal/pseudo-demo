def translate_symbols_to_digits():
    # Read the input string from standard input
    input_string = input().strip()
    
    # Initialize index and result string
    index = 0
    result = ""
    
    # Process each character in the input string
    while index < len(input_string):
        current_symbol = input_string[index]
        
        if current_symbol == '.':
            # Check single dot
            result += '0'
            index += 1  # Move to the next character
        elif index + 1 < len(input_string) and input_string[index + 1] == '.':
            # Check for ".." pattern
            result += '1'
            index += 2  # Skip the next character as well
        elif index + 1 < len(input_string) and input_string[index + 1] == '-':
            # Check for "-." pattern
            result += '2'
            index += 2  # Skip the next character as well
        else:
            # If we encounter an unexpected character, we can handle it
            break  # or you could choose to raise an error
            
    # Output the final result string
    print(result)

# Example call to the function (can be tested with different inputs)
translate_symbols_to_digits()
