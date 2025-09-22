def convert_symbols_to_numbers():
    # Read input from the user
    input_string = input()
    
    # Initialize variables
    index = 0
    result_string = ""
    
    # Process each symbol in the string
    while index < len(input_string):
        current_symbol = input_string[index]
        
        if current_symbol == '.':
            # If current symbol is a dot, append '0'
            result_string += "0"
            index += 1  # Move to the next symbol
        else:
            # Check the next symbol, if available
            if index + 1 < len(input_string):
                next_symbol = input_string[index + 1]
                
                if next_symbol == '.':
                    # If next symbol is also a dot, append '1'
                    result_string += "1"
                    index += 2  # Skip to the symbol after next
                else:
                    # If the next symbol is not a dot, append '2'
                    result_string += "2"
                    index += 2  # Skip to the symbol after next
            else:
                # No next symbol to check, can happen if input ends 
                # on a non-dot symbol
                break
    
    # Output the result
    print(result_string)

# Run the function
convert_symbols_to_numbers()
