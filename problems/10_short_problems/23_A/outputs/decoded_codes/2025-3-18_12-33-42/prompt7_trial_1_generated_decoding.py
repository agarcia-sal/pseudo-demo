def findLongestRepeatedSubstring(inputString):
    # Get the length of the input string
    stringLength = len(inputString)
    # Initialize the length of the longest repeated substring
    longestRepeatedLength = 0

    # Iterate over possible lengths of substrings
    for length in range(1, stringLength):  # Start from 1 to avoid empty substring
        for index in range(stringLength - length):
            # Extract substring of the given length starting from index
            substring = inputString[index:index + length]
            # Check if this substring occurs again after the current index
            if substring in inputString[index + length:]:
                longestRepeatedLength = length  # Update the longest repeated length
                break  # Exit the inner loop if a repetition is found

    # Return the length of the longest repeated substring found
    return longestRepeatedLength

# Input: Read a line of input from the user
userInput = input()
# Output: Call the function with user input and print the result
print(findLongestRepeatedSubstring(userInput))
