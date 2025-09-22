def findLongestRepeatedSubstring(inputString):
    # Remove the trailing newline character from the input string
    trimmedString = removeTrailingNewline(inputString)
    
    # Get the length of the trimmed string
    stringLength = length(trimmedString)
    
    # Initialize the result variable for longest repeated substring length
    longestRepeatedLength = 0

    # Loop through possible substring lengths starting from 0 to stringLength - 1
    for lengthIndex in range(1, stringLength):  # Start from 1 to avoid empty substring
        # Loop over each starting index for the substring
        for startIndex in range(stringLength - lengthIndex + 1):  # Ensure substring does not exceed bounds
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


# Helper function to remove trailing newline character from the input
def removeTrailingNewline(string):
    return string.rstrip('\n')  # Removes any trailing newline character


# Helper function to get the length of a string
def length(string):
    return len(string)  # Returns the number of characters in the string


# Helper function to extract a substring
def substring(string, startIndex, length):
    return string[startIndex:startIndex + length]  # Returns the substring


# Helper function to find the index of a substring in a string
def find(sourceString, subString):
    return sourceString.find(subString)  # Returns the index of subString in sourceString, or -1 if not found


# Usage example (Input handling not shown in the pseudocode context)
