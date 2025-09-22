# Read input string and remove newline character
inputString = input().strip()

# Determine the length of the input string
lengthOfInputString = len(inputString)

# Initialize the variable to track the length of the longest repeated substring
longestRepeatedSubstringLength = 0

# Loop through each possible length of substrings from 1 to lengthOfInputString - 1
for currentLength in range(1, lengthOfInputString):
    # Flag to detect if a repeated substring of this length is found
    foundRepeatedSubstring = False
    
    # Loop through each starting position for the substring
    for startPosition in range(lengthOfInputString - currentLength):
        # Extract the substring from the input string
        substring = inputString[startPosition:startPosition + currentLength]
        
        # Check if the substring can be found later in the input string
        if substring in inputString[startPosition + 1:]:
            longestRepeatedSubstringLength = currentLength
            foundRepeatedSubstring = True
            break  # Break out of the inner loop if a repeat is found
    
    if foundRepeatedSubstring:
        continue  # Continue checking for longer substrings

# Output the length of the longest repeated substring found
print(longestRepeatedSubstringLength)
