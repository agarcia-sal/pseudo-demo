def findLongestRepeatedSubstring(inputString):
    # Initialize the length of the input string
    lengthOfInput = len(inputString)
    longestRepeatLength = 0

    # Loop through possible substring lengths
    for substringLength in range(1, lengthOfInput):  # Start from 1 to avoid empty substring
        for startIndex in range(lengthOfInput - substringLength + 1):  # Ensure the substring fits
            currentSubstring = inputString[startIndex:startIndex + substringLength]

            # Check if the current substring can be found later in the input string
            if currentSubstring in inputString[startIndex + 1:]:
                longestRepeatLength = substringLength  # Update longest repeat length
                break  # No need to check further for this substring length

    return longestRepeatLength

# To execute the function:
line = input()[:-1]  # Take user input and remove the last character
print(findLongestRepeatedSubstring(line))
