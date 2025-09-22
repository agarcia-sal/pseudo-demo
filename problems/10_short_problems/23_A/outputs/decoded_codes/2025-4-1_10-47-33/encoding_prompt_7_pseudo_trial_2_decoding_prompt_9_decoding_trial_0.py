def findLongestRepeatedSubstring(inputString):
    # Get the length of the input string
    stringLength = len(inputString)
    longestRepetitionLength = 0

    # Iterate over possible lengths for substrings from 1 to stringLength - 1
    for l in range(1, stringLength):
        # Iterate over each possible starting index of the substring
        for i in range(stringLength - l):
            # Extract the substring
            substring = inputString[i:i + l]
            # Check if this substring exists later in the string
            if inputString.find(substring, i + 1) != -1:
                # If found, update longest repetition length
                longestRepetitionLength = l
                break  # Exit inner loop if a repetition is found

    # Return the length of the longest repeated substring found
    return longestRepetitionLength
