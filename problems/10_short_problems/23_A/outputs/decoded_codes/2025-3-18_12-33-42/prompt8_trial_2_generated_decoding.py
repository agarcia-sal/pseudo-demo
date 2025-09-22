# Start Program

# Read Input
input_line = input().rstrip()  # Read a line of text and remove the last character (newline)
lengthOfLine = len(input_line)  # Store the length of the line

# Initialize Variables
longestRepeatedSubstringLength = 0  # Variable to track the length of the longest repeated substring

# Outer Loop
for currentLength in range(lengthOfLine):  # For each possible length
    # Inner Loop
    for startIndex in range(lengthOfLine - currentLength):  # For each starting position
        # Substring Extraction
        substring = input_line[startIndex:startIndex + currentLength + 1]  # Extract the substring
        
        # Check for Repeats
        if substring in input_line[startIndex + 1:]:  # Check for repeat after the starting index
            # Update Longest Length
            longestRepeatedSubstringLength = currentLength + 1  # Update the length, accounting for substring length
            break  # Exit the inner loop since we found a repeat

# Output Result
print(longestRepeatedSubstringLength)  # Print the length of the longest repeated substring found
