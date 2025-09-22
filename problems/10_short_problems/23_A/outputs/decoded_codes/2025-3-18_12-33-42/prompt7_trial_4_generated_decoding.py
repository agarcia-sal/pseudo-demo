def findLongestRepeatedSubstring(inputString):
    # Initialize the length of the input string
    lengthOfInput = len(inputString)
    # Initialize variable to store the length of the longest repeated substring found
    longestRepeatedLength = 0

    # Outer loop for possible substring lengths
    for substringLength in range(1, lengthOfInput):  # start from 1 to avoid empty substring
        # Inner loop to extract substrings and check for repetitions
        for index in range(lengthOfInput - substringLength + 1):
            # Extract substring from the input string
            substring = inputString[index:index + substringLength]
            # Check if the substring appears again later in the string
            if substring in inputString[index + 1:]:
                longestRepeatedLength = substringLength  # Update the length found
                break  # Break the inner loop since we found a repeated substring

    return longestRepeatedLength  # Return the length of the longest repeated substring

# Main execution starts here
inputLine = input()  # Read input string from standard input
result = findLongestRepeatedSubstring(inputLine)  # Call the function with the input
print(result)  # Print the result
