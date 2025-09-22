# Function to convert a string of symbols into a numerical string based on specific rules
def convert_symbols_to_numbers():
    # Read input string from user
    input_string = input()
    
    # Initialize variables
    index = 0  # Index to traverse the input string
    result_string = ""  # Resulting string for the number sequence
    
    # Process each symbol in the input string
    while index < len(input_string):
        current_symbol = input_string[index]
        
        if current_symbol == '.':
            # If current symbol is a dot, append "0" and move to next symbol
            result_string += "0"
            index += 1
        else:
            # If the current symbol is not a dot, check the next symbol
            if index + 1 < len(input_string) and input_string[index + 1] == '.':
                # If the next symbol is also a dot, append "1" and move past both symbols
                result_string += "1"
                index += 2
            else:
                # If the next symbol is not a dot, append "2" and move past both symbols
                result_string += "2"
                index += 2
    
    # Output the resulting numerical string
    print(result_string)

# Call the function to execute
convert_symbols_to_numbers()
