def findLongestRepeatedSubstring(inputString):
    # Remove the trailing newline character from the input string
    trimmedString = removeTrailingNewline(inputString)
    
    # Get the length of the trimmed string
    stringLength = length(trimmedString)
    
    # Initialize the result variable for longest repeated substring length
    longestRepeatedLength = 0

    # Loop through possible substring lengths starting from 0 to stringLength - 1
    for lengthIndex in range(1, stringLength):  # Start from 1 to avoid empty substrings
        # Loop over each starting index for the substring
        for startIndex in range(stringLength - lengthIndex + 1):
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

def removeTrailingNewline(string):
    return string.rstrip('\n')

def length(string):
    return len(string)

def substring(string, startIndex, length):
    return string[startIndex:startIndex + length]

def find(sourceString, subString):
    return sourceString.find(subString)

# Usage example
inputString = input()
result = findLongestRepeatedSubstring(inputString)
print(result)
