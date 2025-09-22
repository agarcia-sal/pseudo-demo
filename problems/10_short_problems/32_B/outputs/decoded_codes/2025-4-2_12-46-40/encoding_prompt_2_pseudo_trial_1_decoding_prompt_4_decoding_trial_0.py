# Read a line of input and trim any leading/trailing whitespace
input_string = input().strip()

# Initialize index to track position within input_string
index = 0

# Initialize an empty string to hold the final output
result = ""

# Process the input string while index is less than the string length
while index < len(input_string):
    # Check if the current character is a dot (.)
    if input_string[index] == '.':
        result += '0'  # Append '0' to result
        index += 1  # Move to the next character
    else:
        # Check the next character, if it exists
        if index + 1 < len(input_string) and input_string[index + 1] == '.':
            result += '1'  # Append '1' to result
            index += 2  # Move forward by two characters
        else:
            result += '2'  # Append '2' to result
            index += 2  # Move forward by two characters

# Print the final result
print(result)
