def findLongestRepeatedSubstring(inputString):
    # Get the length of the input string
    lengthOfString = len(inputString)
    # Initialize the variable to store the longest repeated substring length
    longestRepeatedLength = 0

    # Loop through possible substring lengths
    for length in range(1, lengthOfString):
        # Loop through starting indices for the substrings of the current length
        for index in range(lengthOfString - length):
            # Extract the substring from the current index
            substring = inputString[index:index + length]
            
            # Check if the substring appears again after its current position
            if substring in inputString[index + 1:]:
                longestRepeatedLength = length
                break  # Found a repeated substring, break out of the inner loop

    return longestRepeatedLength

# Main Program
inputString = input()  # Read input string from standard input
result = findLongestRepeatedSubstring(inputString)  # Call the function to find the longest repeated substring
print(result)  # Output the result
