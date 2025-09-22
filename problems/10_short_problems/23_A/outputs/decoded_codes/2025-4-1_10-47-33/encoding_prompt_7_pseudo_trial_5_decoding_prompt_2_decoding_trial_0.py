def findLongestRepeatedSubstring(inputString):
    lengthOfInput = len(inputString)
    longestRepeatLength = 0

    for substringLength in range(1, lengthOfInput):  # Starting from 1 to avoid empty substring
        for startIndex in range(lengthOfInput - substringLength + 1):  # Ensures we don't exceed the string's length
            currentSubstring = inputString[startIndex:startIndex + substringLength]

            # Check if currentSubstring exists in the rest of the inputString
            if currentSubstring in inputString[startIndex + 1:]:
                longestRepeatLength = substringLength
                break  # Exit the inner loop as we found a repeated substring

    return longestRepeatLength

# To execute the function:
line = input()[:-1]  # Read input and remove the last character
print(findLongestRepeatedSubstring(line))
