# Start the program

# Receive input
line = input().rstrip()  # Read a line of text and remove trailing newline character
lineLength = len(line)    # Store the length of the line

# Initialize counter for the longest repeated substring length
longestRepeatedSubstringLength = 0

# Iterate over possible substring lengths
for currentLength in range(1, lineLength):  # Start from 1 to avoid empty substring
    # Inner loop to check all starting positions of substrings
    for startIndex in range(lineLength - currentLength + 1):  # Ensure we don't exceed bounds
        substring = line[startIndex:startIndex + currentLength]  # Extract the substring
        
        # Check if this substring appears later in the line
        if substring in line[startIndex + 1:]:  # Look in the part of line after `startIndex`
            # If found, update longest length and break out of the inner loop
            longestRepeatedSubstringLength = currentLength
            break

# Output the result
print(longestRepeatedSubstringLength) # Print the length of the longest repeated substring

# End the program
