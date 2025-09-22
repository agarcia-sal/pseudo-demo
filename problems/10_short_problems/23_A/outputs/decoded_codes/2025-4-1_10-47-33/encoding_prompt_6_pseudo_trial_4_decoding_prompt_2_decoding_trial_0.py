# Read a line of input
stringLine = input().strip()  # Removing any trailing newline characters

# Determine the length of the input line
lengthOfLine = len(stringLine)

# Initialize a variable to store the result
longestRepetitionLength = 0

# Loop over all possible lengths for repeated substrings
for currentLength in range(1, lengthOfLine):  # start from 1 to avoid empty substrings
    # Loop through the string to check for repeated substrings
    for startIndex in range(lengthOfLine):
        # Extract the substring of the current length starting from startIndex
        substring = stringLine[startIndex:startIndex + currentLength]
        
        # Check if the substring appears again in the string after its starting index
        if substring in stringLine[startIndex + 1:]:
            # If found, update the longest repetition length
            longestRepetitionLength = currentLength
            break  # Exit the inner loop if a repetition is found

# Output the length of the longest repeated substring
print(longestRepetitionLength)
