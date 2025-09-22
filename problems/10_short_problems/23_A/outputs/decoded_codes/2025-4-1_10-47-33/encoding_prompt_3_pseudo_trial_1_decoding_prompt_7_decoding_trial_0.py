# Function to find the length of the longest repeated substring
def longest_repeated_substring():
    # Read a line of input from standard input and remove the last character
    stringLine = input()
    stringLine = stringLine[:-1]  # Remove the last character
    lengthOfString = len(stringLine)
    longestRepeatedSubstringLength = 0  # Initialize longest repeated substring length

    # Iterate over possible lengths of substrings
    for substringLength in range(1, lengthOfString):  # Start from 1 to avoid empty substring
        # Check for each starting position of the string
        for startingIndex in range(lengthOfString):
            # Create a substring of the current length starting from startingIndex
            currentSubstring = stringLine[startingIndex:startingIndex + substringLength]

            # Check if the current substring appears again in the string
            if currentSubstring in stringLine[startingIndex + 1:]:
                # Update the longest repeated substring length
                longestRepeatedSubstringLength = substringLength
                break  # Break out of the inner loop if found

    # Output the longest length of the repeated substring found
    print(longestRepeatedSubstringLength)

# Call the function
longest_repeated_substring()
