def translate_symbols_to_numbers():
    # Read input from the user and strip any extra spaces
    symbols = input().strip()
    
    # Initialize variables
    index = 0
    result = ""

    # Process the string while the index is less than the length of the symbols
    while index < len(symbols):
        # Check if the current character is a dot ('.')
        if symbols[index] == '.':
            result += '0'  # Append '0' to result
            index += 1  # Move to the next character
        # Check if the next character is also a dot ('.')
        elif index + 1 < len(symbols) and symbols[index + 1] == '.':
            result += '1'  # Append '1' to result
            index += 2  # Move past both symbols
        else:
            result += '2'  # Append '2' to result for any other cases
            index += 2  # Move past both symbols

    # Output the translated string
    print(result)

# Call the function to execute the translation
translate_symbols_to_numbers()
