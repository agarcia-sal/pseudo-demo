def findLongestRepeatedSubstring(inputString):
    # Initialize the length of the input string
    stringLength = len(inputString)
    # Initialize the variable to store the length of the longest repeated substring
    longestRepeatedLength = 0
    
    # Loop over each possible length of the substring, starting from 0 to stringLength - 1
    for currentLength in range(1, stringLength):  # Start from 1 because a length of 0 isn't meaningful
        # Loop over each starting position of the substring
        for startingIndex in range(stringLength - currentLength):  # Adjust range to prevent overflow
            # Extract the substring of the current length
            substring = inputString[startingIndex:startingIndex + currentLength]
            # Check if the substring exists again in the string after the current starting index
            if substring in inputString[startingIndex + 1:]:
                # Update longestRepeatedLength to currentLength, indicating a repeated substring was found
                longestRepeatedLength = currentLength
                # Exit the inner loop once a repeated substring is found at this length
                break  # Break out of inner FOR loop
        
    # Return the length of the longest repeated substring found
    return longestRepeatedLength

# Read the input
inputString = input()

# Find the longest repeated substring length and print it
result = findLongestRepeatedSubstring(inputString)
print(result)
