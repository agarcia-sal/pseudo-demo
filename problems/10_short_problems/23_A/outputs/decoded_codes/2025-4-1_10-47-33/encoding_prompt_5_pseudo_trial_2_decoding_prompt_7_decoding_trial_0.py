def findLengthOfLongestRepeatingSubstring():
    # Accept input from user
    inputString = readInputString()  # Read a line of input from the user
    stringLength = lengthOf(inputString)  # Calculate the length of the input string
    longestRepeatingLength = 0  # Initialize a variable to store the length of the longest repeating substring

    # Iterate over all possible lengths of substrings
    for substringLength in range(1, stringLength):  # substring length starts from 1 to avoid empty substring
        # Check for each starting position in the string
        for startIndex in range(stringLength - substringLength + 1):  # ensure valid range
            # Extract the substring from current index of specified length
            currentSubstring = extractSubstring(inputString, startIndex, substringLength)

            # Check if this current substring exists later in the inputString
            if existsInString(inputString, currentSubstring, startIndex + 1):
                # If it does exist, update longestRepeatingLength
                longestRepeatingLength = substringLength

    # Output the length of the longest repeating substring found
    print(longestRepeatingLength)

def readInputString():
    # This function reads input from the user
    return input()

def lengthOf(inputStr):
    # This function returns the number of characters in the input string
    return len(inputStr)

def extractSubstring(inputStr, startIndex, length):
    # This function extracts a substring from inputStr starting from startIndex of the specified length
    return inputStr[startIndex:startIndex + length]

def existsInString(inputStr, subStr, startIndex):
    # This function checks if subStr appears in inputStr starting from startIndex
    return subStr in inputStr[startIndex:]

# Calling the main function to execute the logic
findLengthOfLongestRepeatingSubstring()
