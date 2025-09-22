def find_longest_prefix_length():
    # Read a line of input, excluding the last character (newline)
    inputString = input()
    
    # Get the length of the input string
    stringLength = len(inputString)
    
    # Initialize a variable to store the result
    longestPrefixLength = 0
    
    # Loop through potential prefix lengths from 0 up to stringLength - 1
    for currentLength in range(stringLength):
        # Check every starting position in the string
        for startPosition in range(stringLength):
            # Check if the substring starting at startPosition of length currentLength
            # exists again elsewhere in the string
            substring = inputString[startPosition:startPosition + currentLength]
            if inputString.find(substring, startPosition + 1) != -1:
                # Update the longest prefix length if a match is found
                longestPrefixLength = currentLength
                break  # Exit the inner loop if a match is found
    
    # Output the length of the longest prefix found
    print(longestPrefixLength)

# Call the function to execute the logic
find_longest_prefix_length()
