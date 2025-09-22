# Start Program

# Accept Input
inputString = input().strip()  # Read a line of input and remove extra spaces

# Initialize Variables
index = 0                        # Tracks the current position in inputString
result = ""                      # Builds the final output

# Process Input
while index < len(inputString):  # While index is less than the length of inputString
    if inputString[index] == ".":  # If the current character is a dot
        result += "0"               # Append "0" to the result
        index += 1                  # Move to the next position
    elif index + 1 < len(inputString) and inputString[index + 1] == ".":  # If next character is also a dot
        result += "1"                # Append "1" to the result
        index += 2                   # Move ahead by two positions
    else:                           # Otherwise for any other character
        result += "2"               # Append "2" to the result
        index += 2                  # Move ahead by two positions

# Output the Result
print(result)                     # Display the final result
