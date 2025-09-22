# Purpose: This algorithm determines the length of the longest substring that appears more than once in a given line of text.

# Start Program

# Receive Input:
line = input().rstrip()  # Read a line of text from the user and remove any trailing newline characters
lineLength = len(line)   # Store the length of the line in a variable

# Initialize Counter:
longestRepeatedSubstringLength = 0  # This variable will keep track of the longest length found

# Iterate Over Possible Substring Lengths:
for currentLength in range(1, lineLength):  # We start at 1 as length 0 has no meaningful substrings
    for startIndex in range(lineLength - currentLength + 1):  # Adjust so that we can get substrings of `currentLength`
        # Extract the substring from `line`
        substring = line[startIndex:startIndex + currentLength]
        
        # Check if this substring appears later in the line
        if substring in line[startIndex + 1:]:  # Check in the part of the string after `startIndex`
            longestRepeatedSubstringLength = currentLength  # Update the longest length found
            break  # Exit the inner loop as we've found a repeated substring of this length

# Output the Result:
print(longestRepeatedSubstringLength)  # Print the value of longestRepeatedSubstringLength

# End Program
