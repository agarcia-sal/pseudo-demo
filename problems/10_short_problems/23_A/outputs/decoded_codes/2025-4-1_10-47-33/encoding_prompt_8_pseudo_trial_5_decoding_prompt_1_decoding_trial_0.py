# Start

# Read the input line from the user and remove the last character
inputLine = input()[:-1]  # Remove the last character

# Calculate the length of the input line
lengthOfInput = len(inputLine)

# Initialize a variable to keep track of the maximum length of substrings found
longestRepeatedSubstringLength = 0

# Loop through all possible lengths of substrings, starting from 0 to the length of the input line
for substringLength in range(lengthOfInput):  # range until lengthOfInput - 1

    # Loop through each starting position in the string for a substring of the current length
    for startIndex in range(lengthOfInput - substringLength):  # lengthOfInput - substringLength

        # Extract the substring from the input string starting at startIndex with the current length
        currentSubstring = inputLine[startIndex:startIndex + substringLength + 1]  # +1 to include the full length

        # Check if this substring appears again in the input string after startIndex
        if currentSubstring in inputLine[startIndex + 1:]:
            # If found, update the longest substring length variable
            longestRepeatedSubstringLength = substringLength
            # Break out of the loop as we only need the longest length for this size
            break

# Output the maximum length of the repeated substring found
print(longestRepeatedSubstringLength)

# End
