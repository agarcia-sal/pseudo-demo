def findLongestRepeatedSubstring(inputString):
    # Calculate the length of the input string
    lengthOfString = len(inputString)
    # Initialize the variable to track the longest repeated substring length
    longestRepeatedSubstringLength = 0

    # Iterate over possible substring lengths
    for substringLength in range(1, lengthOfString):
        # Iterate over starting indices for substrings of the current length
        for startIndex in range(lengthOfString - substringLength + 1):
            # Extract the current substring
            currentSubstring = inputString[startIndex:startIndex + substringLength]

            # Check if the current substring appears again in the inputString
            # after the current starting index
            if inputString.find(currentSubstring, startIndex + 1) != -1:
                # Update the longest repeated substring length
                longestRepeatedSubstringLength = substringLength
                # Break from the inner loop since we found a repeated substring
                break

    return longestRepeatedSubstringLength

# Driver code to read input from standard input
inputString = input().strip()  # Read input and strip trailing newline characters
print(findLongestRepeatedSubstring(inputString))  # Call the function and output the result
