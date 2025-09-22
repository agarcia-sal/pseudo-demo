# Function to find the length of the longest repeated substring
def longest_repeated_substring():
    # Read a line of input from the user
    stringLine = input().strip()
    
    # Determine the length of the input line
    lengthOfLine = len(stringLine)
    
    # Initialize a variable to store the longest repetition length
    longestRepetitionLength = 0

    # Loop over all possible lengths for repeated substrings
    for currentLength in range(1, lengthOfLine):  # from 1 to lengthOfLine - 1
        # Loop through the string to check for repeated substrings
        for startIndex in range(lengthOfLine - currentLength + 1):  # ensure we stay within bounds
            # Extract the substring of the current length starting from startIndex
            substring = stringLine[startIndex:startIndex + currentLength]

            # Check if the substring appears again in the string after its starting index
            if substring in stringLine[startIndex + currentLength:]:
                # If found, update the longest repetition length
                longestRepetitionLength = currentLength
                break  # Exit the inner loop to check the next length

    # Output the length of the longest repeated substring
    print(longestRepetitionLength)

# Call the function to execute
longest_repeated_substring()
