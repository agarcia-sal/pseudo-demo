def convert_symbols_to_digits():
    # Read the input string of symbols
    symbols = input().strip()
    
    # Initialize variables
    index = 0
    result = ""
    
    # Process the input string while the index is within bounds
    while index < len(symbols):
        current_symbol = symbols[index]
        
        if current_symbol == '.':
            # If it's a single dot, append '0' and move index forward by 1
            result += '0'
            index += 1
        elif current_symbol == '.' and index + 1 < len(symbols) and symbols[index + 1] == '.':
            # If it's a double dot, append '1' and move index forward by 2
            result += '1'
            index += 2
        elif current_symbol == '-' and index + 1 < len(symbols) and symbols[index + 1] == '.':
            # If it's a dash followed by a dot, append '2' and move index forward by 2
            result += '2'
            index += 2
        else:
            # If none of the conditions are met, simply move index forward by 1
            index += 1
            
    # Output the final result string
    print(result)

# Call the function to execute
convert_symbols_to_digits()
