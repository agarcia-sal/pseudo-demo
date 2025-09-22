# Begin the program

# Read a line of input from standard input and remove the last character (newline)
stringInput = input().strip()

# Determine the length of the input string
stringLength = len(stringInput)

# Initialize variable to hold the result
longestRepeatedSubstringLength = 0

# Loop through lengths of potential substrings from 0 to stringLength - 1
for lengthFromZero in range(stringLength):

    # Loop through each starting index for the substrings
    for startIndex in range(stringLength):

        # Extract the substring from startIndex of the current length
        currentSubstring = stringInput[startIndex:startIndex + lengthFromZero]

        # Check if the current substring can be found in the remainder of the string
        if currentSubstring in stringInput[startIndex + 1:]:

            # If found, update the result to the current length
            longestRepeatedSubstringLength = lengthFromZero

            # Exit the loop since we found a repeated substring of this length
            break

    # If we found a repeated substring of this length, break the outer loop
    if longestRepeatedSubstringLength == lengthFromZero:
        break

# Output the length of the longest repeated substring found
print(longestRepeatedSubstringLength)

# End the program
