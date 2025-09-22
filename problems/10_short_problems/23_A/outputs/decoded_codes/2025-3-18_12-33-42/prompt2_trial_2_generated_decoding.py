# Input
inputString = input().strip()  # Read a line of text and remove trailing newline
stringLength = len(inputString)  # Determine the length of the input string
longestRepeatedSubstringLength = 0  # Initialize the longest repeated substring length

# Process
for currentLength in range(1, stringLength):  # Loop over each possible substring length
    for startIndex in range(stringLength - currentLength + 1):  # Loop for each starting position
        substring = inputString[startIndex:startIndex + currentLength]  # Extract the substring
        # Check if the substring occurs again in the rest of the inputString
        if substring in inputString[startIndex + 1:]:
            longestRepeatedSubstringLength = currentLength  # Update the length of the longest repeated substring
            break  # Exit inner loop as we found a repeated substring

# Output
print(longestRepeatedSubstringLength)  # Print the length of the longest repeated substring
