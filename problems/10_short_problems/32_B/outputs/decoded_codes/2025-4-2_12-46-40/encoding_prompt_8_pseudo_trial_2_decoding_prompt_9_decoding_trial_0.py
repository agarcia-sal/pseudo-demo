# Read input: Get a string of symbols from user input and strip extra spaces
input_string = input().strip()

# Initialize variables
index = 0  # To track the current position in the string
result = ""  # To store the translated numbers

# Process the string while the index is less than the length of the string
while index < len(input_string):
    # Check if the character at the current index is a dot ('.')
    if input_string[index] == '.':
        result += '0'  # Append '0' to result for a single dot
        index += 1  # Move to the next character
    # Check if the next character is also a dot ('.')
    elif index + 1 < len(input_string) and input_string[index + 1] == '.':
        result += '1'  # Append '1' for a dot followed by another dot
        index += 2  # Move past the two symbols
    else:
        result += '2'  # Default case for any other symbol
        index += 2  # Move past the two symbols

# Output result: Display the translated string
print(result)
