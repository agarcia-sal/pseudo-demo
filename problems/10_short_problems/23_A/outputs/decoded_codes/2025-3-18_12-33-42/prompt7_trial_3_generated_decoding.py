def findLongestRepeatedSubstring(inputString):
    # Initialize the length of the longest repeated substring to zero
    substringLength = 0
    # Get the length of the input string
    stringLength = len(inputString)

    # Loop over each possible length of substring
    for length in range(1, stringLength):  # Starting from 1 since length of 0 has no valid substrings
        # Loop over each starting index for the substring
        for index in range(stringLength - length + 1):  # Ensure we don't go out of bounds
            # Get the current substring
            currentSubstring = inputString[index:index + length]
            # Check if the current substring exists in the rest of the string
            if currentSubstring in inputString[index + 1:]:
                # If found, update the substringLength
                substringLength = length
                break  # Break out of the inner loop since we found a repeated substring

    return substringLength

# Read input string from standard input
userInputString = input()
# Call the function to find the length of the longest repeated substring
result = findLongestRepeatedSubstring(userInputString)
# Print the result
print(result)
