# Start the Program

# Read Input
input_string = input().strip()  # Trim excess whitespace

# Initialize Variables
index = 0  # Counter to track the current position in the input string
result = ""  # To store the final output sequence

# Process the Input String
while index < len(input_string):  # Loop until the end of input_string
    if input_string[index] == '.':  # Check if current character is a dot
        result += '0'  # Append '0' to result
        index += 1  # Move to the next character
    elif index + 1 < len(input_string) and input_string[index + 1] == '.':  # Check next character
        result += '1'  # Append '1' to result
        index += 2  # Skip the next character
    else:  # If the current character is not a dot and next isn't either
        result += '2'  # Append '2' to result
        index += 2  # Skip the next character

# Output the Result
print(result)  # Print the final output
