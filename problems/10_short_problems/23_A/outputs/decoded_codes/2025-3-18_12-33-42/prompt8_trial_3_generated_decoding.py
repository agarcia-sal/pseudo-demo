# Start the program

# Read Input
input_string = input()
lengthOfInput = len(input_string)

# Initialize Variable
longestRepeatedSubstringLength = 0

# Loop Through Substring Lengths
for lengthFromZero in range(lengthOfInput):
    # Loop for Each Starting Character Index
    for currentIndex in range(lengthOfInput):
        # Extract a Substring
        subString = input_string[currentIndex:currentIndex + lengthFromZero]
        
        # Check for Duplicate
        if subString and subString in input_string[currentIndex + 1:]:
            longestRepeatedSubstringLength = lengthFromZero
            break  # Break out of the inner loop

# Output Result
print(longestRepeatedSubstringLength)

# End the program
