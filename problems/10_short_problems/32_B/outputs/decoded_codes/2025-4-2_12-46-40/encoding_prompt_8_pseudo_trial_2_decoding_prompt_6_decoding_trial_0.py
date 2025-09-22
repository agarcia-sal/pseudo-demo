# Start of the code

# Read Input:
# Get a string of symbols from user input, trimming any extra spaces
input_string = input().strip()

# Initialize Variables:
# Set a counter to track the current position in the string
index = 0
# Create an empty string to store the translated numbers
result = ""

# Process the String:
# While the counter index is less than the length of the string
while index < len(input_string):
    # If the character at the current index is a dot ('.')
    if input_string[index] == '.':
        # Append '0' to result
        result += '0'
        # Increment index by 1 to move to the next character
        index += 1
    # Else if the character at the current index plus one is a dot ('.')
    elif index + 1 < len(input_string) and input_string[index + 1] == '.':
        # Append '1' to result
        result += '1'
        # Increment index by 2 to move past the two symbols
        index += 2
    else:
        # Append '2' to result
        result += '2'
        # Increment index by 2 to move past the two symbols
        index += 2

# Output Result:
# Display the translated string result
print(result)

# End of the code
