# Start Program

# Read Input
input_line = input()[:-1]  # Remove the last character (newline)

# Determine Length
lengthOfLine = len(input_line)

# Initialize Variable
longestSubstringLength = 0  # This will store the length of the longest repeated substring found

# Iterate Over Possible Substring Lengths
for currentSubstringLength in range(lengthOfLine):  # from 0 to lengthOfLine - 1
    # Check for Repeated Substrings
    for startIndex in range(lengthOfLine):  # from 0 to lengthOfLine - 1
        # Extract the substring
        substring = input_line[startIndex:startIndex + currentSubstringLength]

        # Check if substring appears again
        if substring in input_line[startIndex + 1:]:  # Look for the substring after the current position
            # Update longestSubstringLength
            longestSubstringLength = currentSubstringLength
            break  # found a repeat, exit the inner loop

# Output Result
print(longestSubstringLength)  # Print the length of the longest repeated substring found

# End Program
