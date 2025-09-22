# 1. Receive Input:
inputString = input().strip()  # Read a line of input and remove surrounding whitespace.

# 2. Initialize Variables:
index = 0                        # Set index to track the current position in the input string.
outputString = ""                # Create an empty string for the output representation.

# 3. Process the Input String:
while index < len(inputString):  # While index is less than the length of inputString:
    if inputString[index] == '.':  # If the character at inputString[index] is a dot:
        outputString += '0'          # Append '0' to outputString.
        index += 1                   # Increment index by 1.
    elif index + 1 < len(inputString) and inputString[index + 1] == '.':  # Check next character for dot.
        outputString += '1'          # Append '1' to outputString.
        index += 2                   # Increment index by 2 to skip the next character.
    else:                            # Otherwise:
        outputString += '2'          # Append '2' to outputString.
        index += 2                   # Increment index by 2 to skip the next character.

# 4. Output the Result:
print(outputString)                # Print the resulting numerical representation.
