# Read a string of symbols representing the input sequence
input_string = input()

# Initialize an index to track the current position in the input string
index = 0
# Initialize an empty result string to hold the final output digits
result_string = ""

# Process the input string while the index is less than the length of the input string
while index < len(input_string):
    current_symbol = input_string[index]  # Get the current symbol

    # Check if the current symbol is a dot
    if current_symbol == '.':
        result_string += '0'  # Append '0' for a single dot
        index += 1  # Move to the next symbol
    # Check if the next symbol exists and is also a dot
    elif index + 1 < len(input_string) and input_string[index + 1] == '.':
        result_string += '1'  # Append '1' for a pair of dots
        index += 2  # Move past both symbols
    # At this point, we are guaranteed the current symbol is a dash
    elif index + 1 < len(input_string):
        result_string += '2'  # Append '2' for a dash followed by a dot
        index += 2  # Move past both symbols

# Output the final result string
print(result_string)
