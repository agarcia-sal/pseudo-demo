# Start the program

# Accept input from the user
inputString = input().strip()  # Read input and remove extra spaces or new lines

# Initialize variables
index = 0  # Track the current position in inputString
result = ""  # Create an empty string to build the final output

# Process input
while index < len(inputString):  # While index is less than the length of inputString
    if inputString[index] == ".":  # If current character is a dot
        result += "0"  # Append "0" to the result
        index += 1  # Move to the next position
    elif index + 1 < len(inputString) and inputString[index + 1] == ".":  # Check next position if in bounds
        result += "1"  # Append "1" to the result
        index += 2  # Move ahead by two positions
    else:
        result += "2"  # Append "2" to the result
        index += 2  # Move ahead by two positions

# Output the result
print(result)  # Display the final result string
