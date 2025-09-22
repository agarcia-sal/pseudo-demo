# Start of the program

# Read the input line from the user and remove the last character (usually a newline).
inputLine = input().rstrip()  # .rstrip() removes any trailing whitespace or newline

# Calculate the length of the input line.
lengthOfInput = len(inputLine)

# Initialize a variable to keep track of the maximum length of substrings found.
longestRepeatedSubstringLength = 0

# Loop through all possible lengths of substrings, starting from 0 to the length of the input line.
for substringLength in range(lengthOfInput):
    
    # Loop through each starting position in the string for a substring of the current length.
    for startIndex in range(lengthOfInput - substringLength):
        
        # Extract the substring from the input string starting at startIndex with the current length.
        currentSubstring = inputLine[startIndex:startIndex + substringLength + 1]

        # Check if this substring appears again in the input string, starting from the position after startIndex.
        if inputLine.find(currentSubstring, startIndex + 1) != -1:
            # If found, update the longest substring length variable.
            longestRepeatedSubstringLength = substringLength + 1  # Add 1 to substringLength for length
            # Break out of the loop as we only need the longest length for this size.
            break

# Output the maximum length of the repeated substring found.
print(longestRepeatedSubstringLength)

# End of the program
