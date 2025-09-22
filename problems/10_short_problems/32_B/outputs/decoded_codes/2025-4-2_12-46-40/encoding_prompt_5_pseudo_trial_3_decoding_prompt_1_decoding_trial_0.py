# 1. Start Program

# 2. Accept Input:
inputString = input().strip()  # Read input and remove extra spaces/newlines.

# 3. Initialize Variables:
index = 0  # Track the current position in inputString
result = ""  # Build the final output

# 4. Process Input:
while index < len(inputString):  # While the index is less than length of inputString
    if inputString[index] == ".":  # If current character is a dot
        result += "0"  # Append "0" to result
        index += 1  # Move to the next position
    elif index + 1 < len(inputString) and inputString[index + 1] == ".":  # If next character is also a dot
        result += "1"  # Append "1" to result
        index += 2  # Move ahead by two positions
    else:  # Otherwise
        result += "2"  # Append "2" to result
        index += 2  # Move ahead by two positions

# 5. Output the Result:
print(result)  # Display final result
