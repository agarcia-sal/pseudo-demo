def convert_symbols_to_digits():
    # Read a string of symbols from standard input
    symbols = input()
    
    # Initialize index to track position in the input string
    index = 0
    
    # Initialize an empty result string to hold the output digits
    result_digits = ""
    
    # Process the input string while the index is within bounds
    while index < len(symbols):
        current_symbol = symbols[index]
        
        # Check the current symbol and the next symbol
        if current_symbol == '.':
            # Single dot corresponds to '0'
            result_digits += '0'
            index += 1  # Move to the next symbol
        elif index + 1 < len(symbols) and symbols[index + 1] == '.':
            # Pair of dots corresponds to '1'
            result_digits += '1'
            index += 2  # Skip both symbols
        elif index + 1 < len(symbols) and symbols[index + 1] == '-':
            # A dash followed by a dot corresponds to '2'
            result_digits += '2'
            index += 2  # Skip both symbols
        else:
            # Handle unexpected symbol (optional, based on requirements)
            # Since the problem assumes valid input, this part may not be needed

            index += 1  # Move to the next symbol

    # Output the final result string
    print(result_digits)

# The function would be called to execute the conversion
convert_symbols_to_digits()
