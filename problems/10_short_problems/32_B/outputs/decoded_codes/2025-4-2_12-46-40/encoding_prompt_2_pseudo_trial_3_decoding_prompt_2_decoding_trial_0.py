# Read a string of characters representing a sequence of symbols
input_string = input()

# Initialize index variable and result string
index = 0
result = ""

# Process the input string
while index < len(input_string):
    # Check the current symbol at the index
    current_symbol = input_string[index]
    
    if current_symbol == '.':
        result += '0'  # A single dot corresponds to the digit '0'
        index += 1     # Move to the next symbol
    elif index + 1 < len(input_string) and input_string[index + 1] == '.':
        result += '1'  # A pair of dots corresponds to '1'
        index += 2     # Move past both symbols
    else:
        result += '2'  # A dash followed by a dot corresponds to '2'
        index += 2     # Move past both symbols

# Output the final result string containing all of the digits
print(result)
