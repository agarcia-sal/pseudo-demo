def translate_symbols_to_numbers():
    # Read input from the user and remove any leading or trailing spaces
    input_string = input().strip()
    
    # Initialize variables
    index = 0
    result = ""

    # Process the input string
    while index < len(input_string):
        if input_string[index] == '.':
            result += '0'  # Append '0' for a single dot
            index += 1     # Move to the next character
        elif index + 1 < len(input_string) and input_string[index + 1] == '.':
            result += '1'  # Append '1' for a dot followed by another dot
            index += 2     # Move past the two symbols
        else:
            result += '2'  # Append '2' for other combinations
            index += 2     # Move past the two symbols

    # Output the result
    print(result)

# Call the function to run the translation
translate_symbols_to_numbers()
