def findLongestRepeatedSubstringLength():
    # Read input string from the user
    inputString = input()
    stringLength = len(inputString)
    longestRepeatedLength = 0  # Initialize variable for the longest repeated substring length

    # Iterate over possible substring lengths from 0 to stringLength - 1
    for substringLength in range(stringLength):  # from 0 to stringLength - 1
        # Check each starting position for a substring of the current length
        for startPosition in range(stringLength):  # from 0 to stringLength - 1
            # Extract the substring from the current start position of the defined length
            currentSubstring = inputString[startPosition:startPosition + substringLength]
            
            # Check if this substring occurs again in the string after the current position
            if currentSubstring in inputString[startPosition + 1:]:
                # Update the longest repeated length if we found a longer one
                longestRepeatedLength = substringLength
                break  # No need to check other start positions for this length

    # Output the length of the longest repeated substring found
    print(longestRepeatedLength)

# Invoke the function (commented out to avoid accidental execution)
# findLongestRepeatedSubstringLength()
