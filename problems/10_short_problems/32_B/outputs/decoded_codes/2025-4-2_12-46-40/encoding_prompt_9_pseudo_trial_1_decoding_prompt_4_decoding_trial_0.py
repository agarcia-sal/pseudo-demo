def convert_symbols_to_numbers():
    # Step 1: Read input from user
    input_string = input()
    
    # Step 2: Initialize variables
    index = 0
    result = ""

    # Step 3: Process each symbol
    while index < len(input_string):
        current_symbol = input_string[index]
        
        if current_symbol == ".":
            # Append '0' if current symbol is a dot
            result += "0"
            index += 1  # Move to the next symbol
        else:
            # Check the next symbol if the current is not a dot
            if index + 1 < len(input_string):
                next_symbol = input_string[index + 1]
                if next_symbol == ".":
                    # Append '1' if the next symbol is a dot
                    result += "1"
                    index += 2  # Skip to the next pair of symbols
                else:
                    # Append '2' if the next symbol is not a dot
                    result += "2"
                    index += 2  # Skip to the next pair of symbols
            else:
                # If there's no next symbol, handle it gracefully
                break

    # Step 4: Output the result
    print(result)

# Call the function to execute the code
convert_symbols_to_numbers()
