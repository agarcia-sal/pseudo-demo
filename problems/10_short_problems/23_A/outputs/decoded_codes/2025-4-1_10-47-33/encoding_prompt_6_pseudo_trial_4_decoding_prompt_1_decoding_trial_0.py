# Read a line of input and remove the trailing newline character
stringLine = input()

# Determine the length of the input line
lengthOfLine = len(stringLine)

# Initialize a variable to store the result
longestRepetitionLength = 0

# Loop over all possible lengths for repeated substrings
for currentLength in range(lengthOfLine):
    # Loop through the string to check for repeated substrings
    for startIndex in range(lengthOfLine):
        # Extract the substring of the current length starting from startIndex
        substring = stringLine[startIndex:startIndex + currentLength + 1]

        # Check if the substring appears again in the string after its starting index
        if substring in stringLine[startIndex + 1:]:
            # If found, update the longest repetition length
            longestRepetitionLength = currentLength
            break  # Break out of the inner loop
            
# Output the length of the longest repeated substring
print(longestRepetitionLength)
