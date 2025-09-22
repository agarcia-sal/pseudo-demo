def convert_symbols_to_numbers():
    # Read input from the user
    symbols = input()
    
    # Initialize variables
    index = 0
    result = ""
    
    # Process each symbol in the input string
    while index < len(symbols):
        if symbols[index] == '.':
            result += "0"  # Append '0' for a single dot
            index += 1     # Move to the next symbol
        else:
            if index + 1 < len(symbols) and symbols[index + 1] == '.':
                result += "1"  # Append '1' for the pattern 'symbol followed by dot'
                index += 2     # Skip to the next pair of symbols
            else:
                result += "2"  # Append '2' for 'symbol followed by non-dot'
                index += 2     # Skip to the next pair of symbols

    # Output the result
    print(result)

# Run the function
convert_symbols_to_numbers()
