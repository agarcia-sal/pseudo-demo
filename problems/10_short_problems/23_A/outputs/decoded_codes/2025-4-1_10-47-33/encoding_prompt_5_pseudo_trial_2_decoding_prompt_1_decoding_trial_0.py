def findLengthOfLongestRepeatingSubstring():
    # Accept input from user
    inputString = readInputString()  # Read a line of input from the user
    stringLength = lengthOf(inputString)  # Calculate the length of the input string
    longestRepeatingLength = 0  # Initialize a variable to store the length of the longest repeating substring

    # Iterate over all possible lengths of substrings
    for substringLength in range(stringLength):  # from 0 to stringLength - 1
        # Check for each starting position in the string
        for startIndex in range(stringLength):  # from 0 to stringLength - 1
            # Extract the substring from current index of specified length
            currentSubstring = extractSubstring(inputString, startIndex, substringLength)

            # Check if this current substring exists later in the inputString
            if existsInString(inputString, currentSubstring, startIndex + 1):  
                # If it does exist, update longestRepeatingLength
                longestRepeatingLength = substringLength
                break  # Stop checking this length since we've already found a match

    # Output the length of the longest repeating substring found
    print(longestRepeatingLength)


def readInputString():
    return input()  # read a line of input from the user


def lengthOf(inputStr):
    return len(inputStr)  # return the number of characters in str


def extractSubstring(inputStr, startIndex, length):
    return inputStr[startIndex:startIndex + length]  # return substring of inputStr starting from startIndex of specified length


def existsInString(inputStr, subStr, startIndex):
    # Check if subStr appears in inputStr starting from startIndex
    return inputStr.find(subStr, startIndex) != -1  # return true if subStr can be found in inputStr starting from startIndex, otherwise return false
