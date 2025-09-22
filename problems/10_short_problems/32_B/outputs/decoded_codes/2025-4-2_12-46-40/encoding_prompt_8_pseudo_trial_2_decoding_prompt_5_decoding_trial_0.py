# Function to translate a string of symbols into a numeric representation
def translate_symbols():
    # Read input string, stripping any extra spaces
    symbols = input().strip()
    
    # Initialize the index to track position in the string and result to store output
    index = 0
    result = ""

    # Process the string
    while index < len(symbols):
        # Check if the current character is a dot
        if symbols[index] == '.':
            result += '0'  # Append '0' for a single dot
            index += 1     # Move to next character
        # Check for a dot followed by another symbol
        elif index + 1 < len(symbols) and symbols[index + 1] == '.':
            result += '1'  # Append '1' for a combination of symbols
            index += 2     # Move past these two characters
        else:
            result += '2'  # Default case for no dots found
            index += 2     # Move past these two characters
    
    # Output the translated result
    print(result)

# Example test case (uncomment to test):
# Example input: "..**.."
# Expected output: "0012"
