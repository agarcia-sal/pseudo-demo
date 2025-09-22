# Start Program

# Accept Input: Read a line from the user and clean it
inputString = input().strip()

# Initialize Variables
index = 0  # Track the current position in inputString
result = ""  # Initialize an empty string for the output

# Process Input
while index < len(inputString):  # Continue until the end of the string
    if inputString[index] == ".":  # If the current character is a dot
        result += "0"  # Append "0" to the result
        index += 1  # Move to the next character
    elif index + 1 < len(inputString) and inputString[index + 1] == ".":  # If the next character is also a dot
        result += "1"  # Append "1" to the result
        index += 2  # Move ahead by two positions
    else:  # For any other character
        result += "2"  # Append "2" to the result
        index += 2  # Move ahead by two positions

# Output the Result
print(result)  # Display the final result string
