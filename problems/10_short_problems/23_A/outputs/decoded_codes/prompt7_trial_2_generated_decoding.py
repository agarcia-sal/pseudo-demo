def findLongestPrefixLength(inputString):
    # Get the length of the input string
    stringLength = len(inputString)
    # Initialize the longest prefix length to 0
    longestPrefixLength = 0

    # Iterate over possible prefix lengths
    for prefixLength in range(stringLength):
        # Iterate over starting indices of the string
        for startIndex in range(stringLength):
            # Get the current prefix substring
            currentPrefix = inputString[startIndex:startIndex + prefixLength]
            # Check if the current prefix appears again in the string
            if inputString.find(currentPrefix, startIndex + 1) != -1:
                # Update the longest prefix length
                longestPrefixLength = prefixLength
                # Break out of the inner loop since we found a valid prefix
                break

    # Return the length of the longest prefix found
    return longestPrefixLength

# Read input from standard input
userInput = input()
# Execute the function and store the result
result = findLongestPrefixLength(userInput)
# Print the result
print(result)
