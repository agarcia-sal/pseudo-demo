def findLongestRepeatedSubstringLength():
    # Read input from standard input and remove the newline character
    input_string = input().strip()
    lengthOfInput = len(input_string)  # Store the length of the input
    longestRepeatedSubstringLength = 0  # Initialize the length of the longest repeating substring

    # Check for substrings of increasing length
    for currentLength in range(lengthOfInput):
        # Iterate through the starting index of the substring
        for startIndex in range(lengthOfInput):
            # Create a substring of length (currentLength + 1)
            substring = input_string[startIndex:startIndex + currentLength + 1]
            # Check if this substring appears again in the input after the startIndex
            if input_string.find(substring, startIndex + 1) != -1:
                # Update the longest repeating substring length
                longestRepeatedSubstringLength = currentLength + 1
                break  # Exit the inner loop since we found a repeat

    # Output the length of the longest repeating substring
    print(longestRepeatedSubstringLength)

# To test the function, you can uncomment the next line and provide input directly in the terminal.
# findLongestRepeatedSubstringLength()
