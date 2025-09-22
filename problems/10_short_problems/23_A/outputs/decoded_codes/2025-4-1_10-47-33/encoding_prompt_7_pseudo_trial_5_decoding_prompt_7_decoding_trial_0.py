def findLongestRepeatedSubstring(inputString):
    # Initialize the length of the input string
    lengthOfInput = len(inputString)
    longestRepeatLength = 0  # To track the length of the longest repeated substring

    # Iterate over possible substring lengths
    for substringLength in range(lengthOfInput + 1):
        # Check each starting index for the substring
        for startIndex in range(lengthOfInput):
            # Get the current substring from the input string
            currentSubstring = inputString[startIndex:startIndex + substringLength]
            
            # Check if the substring can be found later in the string
            if currentSubstring in inputString[startIndex + 1:]:
                longestRepeatLength = substringLength  # Update the longest repeat length
                break  # Exit the inner loop as we found a repeated substring

    return longestRepeatLength  # Return the length of the longest repeated substring

# Execute the function
line = input()[:-1]  # Read input and remove the last character
print(findLongestRepeatedSubstring(line))  # Output the result
