def findLongestRepeatedSubstring(inputString):
    # Get the length of the input string
    stringLength = len(inputString)
    longestRepetitionLength = 0

    # Iterate over possible lengths for substrings from 0 to stringLength - 1
    for l in range(stringLength):
        # Iterate over each possible starting index of the substring
        for i in range(stringLength):
            # Check if the substring starting at index i with length l exists later in the string
            if inputString.find(inputString[i:i + l], i + 1) != -1:
                # If found, update longest repetition length
                longestRepetitionLength = l
                break  # Exit inner loop if a repetition is found

    # Return the length of the longest repeated substring found
    return longestRepetitionLength
