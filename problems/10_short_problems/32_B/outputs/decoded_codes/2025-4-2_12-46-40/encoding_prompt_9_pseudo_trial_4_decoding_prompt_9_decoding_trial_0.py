# Start the Program

# Read Input
inputString = input().strip()  # Receive a single line of input and trim excess whitespace

# Initialize Variables
index = 0  # Counter to traverse the string
result = ""  # Resultant string to store the output

# Process the Input String
while index < len(inputString):
    if inputString[index] == '.':
        result += '0'  # Append '0' for a single dot
        index += 1  # Move to the next character
    elif index + 1 < len(inputString) and inputString[index + 1] == '.':
        result += '1'  # Append '1' for two dots in succession
        index += 2  # Skip the next character
    else:
        result += '2'  # Append '2' for any other character
        index += 2  # Skip the next character

# Output the Result
print(result)  # Print the final value of result
