def findLongestRepeatedSubstring(inputString):
    # Helper function to remove trailing newline character from the input
    def removeTrailingNewline(string):
        return string.rstrip('\n')  # Remove trailing newline characters

    # Helper function to get the length of a string
    def length(string):
        return len(string)  # Return the number of characters in the string

    # Helper function to extract a substring
    def substring(string, startIndex, length):
        return string[startIndex:startIndex + length]  # Extract substring based on indices

    # Helper function to find the index of a substring in a string
    def find(sourceString, subString):
        return sourceString.find(subString)  # Returns the index of subString, or -1 if not found

    # Remove the trailing newline character from the input string
    trimmedString = removeTrailingNewline(inputString)

    # Get the length of the trimmed string
    stringLength = length(trimmedString)

    # Initialize variable for the length of the longest repeated substring
    longestRepeatedLength = 0

    # Loop through possible substring lengths from 1 to stringLength
    for lengthIndex in range(1, stringLength):
        # Loop over each starting index for the substring
        for startIndex in range(stringLength - lengthIndex):
            # Extract the current substring based on lengthIndex and startIndex
            currentSubstring = substring(trimmedString, startIndex, lengthIndex)

            # Check if the current substring exists later in the string
            if find(trimmedString, currentSubstring) != -1:
                # If found, update longestRepeatedLength with the current length
                longestRepeatedLength = lengthIndex
                # Exit the inner loop as we found a repeated substring
                break

    # Return the length of the longest repeated substring found
    return longestRepeatedLength

# Example usage (input reading is done externally)
inputString = input()  # Read input string from user
result = findLongestRepeatedSubstring(inputString)
print(result)  # Output the length of the longest repeated substring
