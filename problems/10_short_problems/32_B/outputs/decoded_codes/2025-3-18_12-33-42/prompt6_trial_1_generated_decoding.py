# Start of the program

# Read input string from standard input
input_string = input()

# Initialize the index and the result variable
index = 0
result = ""  # Storing the final result as an empty string

# Loop until the end of the string
while index < len(input_string):
    # Check the character at the current index
    if input_string[index] == '.':
        # Append '0' to the result
        result += '0'
        # Move to the next character
        index += 1
    else:
        # Check the next character
        if index + 1 < len(input_string) and input_string[index + 1] == '.':
            # Append '1' to the result
            result += '1'
            # Move two characters ahead
            index += 2
        else:
            # Append '2' to the result
            result += '2'
            # Move two characters ahead
            index += 2

# Print the result string
print(result)

# End of the program
