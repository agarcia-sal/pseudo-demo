def translate_symbols_to_numbers():
    # Read input string, trimming any leading/trailing whitespace
    input_string = input().strip()
    
    # Initialize counter and result variables
    index = 0
    result = ""
    
    # Process the string based on the defined rules
    while index < len(input_string):
        if input_string[index] == '.':
            result += '0'  # If current character is a dot, append '0'
            index += 1     # Move to the next character
        elif index + 1 < len(input_string) and input_string[index + 1] == '.':
            result += '1'  # If the next character is a dot, append '1'
            index += 2     # Move past the two symbols
        else:
            result += '2'  # In all other cases, append '2'
            index += 2     # Move past the two symbols

    # Output the result
    print(result)

# Call the function to execute the translation
translate_symbols_to_numbers()
