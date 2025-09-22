# Read a line of input and remove the trailing newline character
stringLine = input().strip()

# Determine the length of the input line
lengthOfLine = len(stringLine)

# Initialize a variable to store the result
longestRepetitionLength = 0

# Loop over all possible lengths for repeated substrings
for currentLength in range(1, lengthOfLine):  # start at 1 to avoid empty substring
    # Loop through the string to check for repeated substrings
    for startIndex in range(lengthOfLine - currentLength):  # ensure we don't go out of bounds
        # Extract the substring of the current length starting from startIndex
        substring = stringLine[startIndex:startIndex + currentLength]

        # Check if the substring appears again in the string after its starting index
        if substring in stringLine[startIndex + currentLength:]:
            # If found, update the longest repetition length
            longestRepetitionLength = currentLength
            break  # Exit inner loop if repetition found

# Output the length of the longest repeated substring
print(longestRepetitionLength)
