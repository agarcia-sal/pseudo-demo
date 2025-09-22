# Start the Program

# Read Input:
inputString = input().strip()  # Get a line of text and remove leading/trailing spaces

# Initialize Variables:
index = 0                        # Set a counter to track the position in the string
result = ""                      # Create an empty string for the numeric output

# Process the String:
while index < len(inputString):  # While index is less than the length of inputString
    # Check Current Character
    if inputString[index] == '.':  # If the current character is a dot
        result += '0'               # Append '0' to result
        index += 1                  # Increase index by 1
    # Check Next Character
    elif index + 1 < len(inputString) and inputString[index + 1] == '.':  # Check next character is also a dot
        result += '1'               # Append '1' to result
        index += 2                  # Increase index by 2
    # Default Case
    else:                          # Otherwise
        result += '2'               # Append '2' to result
        index += 2                  # Increase index by 2

# Output the Result:
print(result)                    # Display the final result string
