def findLongestRepeatedSubstring(inputString):
    # Remove newline characters from the input string
    trimmedString = inputString.strip()
    
    # Get the length of the input string
    stringLength = len(trimmedString)
    
    # Initialize variable to store the maximum length of the repeated substring
    longestRepeatedLength = 0
    
    # Loop through possible substring lengths from 1 to stringLength
    for substringLength in range(1, stringLength):
        # Loop through all starting positions for the substring
        for startIndex in range(stringLength - substringLength):
            # Extract the current substring
            currentSubstring = trimmedString[startIndex:startIndex + substringLength]
            
            # Check if this substring exists in the string starting from the next position
            if currentSubstring in trimmedString[startIndex + 1:]:
                # Update longestRepeatedLength if a repeated substring is found
                longestRepeatedLength = substringLength
                break  # Exit the inner loop since a repetition is found
        # Check to ensure we move to the next substring length
    return longestRepeatedLength

# Input: Read a line from standard input
inputLine = input()

# Output: Call the function and print the result
outputLength = findLongestRepeatedSubstring(inputLine)
print(outputLength)
