# BEGIN PROGRAM

# Read input from standard input, then trim any whitespace
stringRepresentation = input().strip()

# Initialize variables
index = 0  # Index to track the current position in the string
resultString = ""  # Result string to accumulate the output

# Continue processing until we reach the end of the string
while index < len(stringRepresentation):
    # Check the current character at the index
    if stringRepresentation[index] == '.':
        # If current character is '.', append '0' to the result
        resultString += '0'
        index += 1  # Move to the next character
    elif index + 1 < len(stringRepresentation) and stringRepresentation[index + 1] == '.':
        # If the next character is also '.', append '1' to the result
        resultString += '1'
        index += 2  # Move past both dots
    else:
        # If neither condition is satisfied, append '2' to the result
        resultString += '2'
        index += 2  # Move to the next character that hasn't been processed

# Output the final result string
print(resultString)

# END PROGRAM
