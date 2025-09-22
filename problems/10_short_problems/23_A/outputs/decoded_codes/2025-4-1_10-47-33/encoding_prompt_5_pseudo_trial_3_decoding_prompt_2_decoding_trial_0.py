# Read a line of input from the user
line = input()

# Remove the newline character from the end of the input
line = line.strip()  # This will also handle removal of trailing newline characters

# Calculate the length of the input string
n = len(line)

# Initialize a variable to hold the length of the longest repeated substring
longestRepeatedLength = 0

# Loop through substrings of increasing lengths
for length in range(1, n):  # Starting from length 1 to n-1
    # Check all starting positions for the substring of the current length
    for startPosition in range(n - length + 1):  # Valid start positions for the given length
        # Extract the substring from 'startPosition'
        currentSubstring = line[startPosition:startPosition + length]

        # Check if this substring appears again in the string after its starting position
        if line.find(currentSubstring, startPosition + 1) != -1:
            # If the substring is found again, update the longest repeated length
            longestRepeatedLength = length
            break  # Exit this inner loop as we found a repeat

# Print the length of the longest repeated substring found
print(longestRepeatedLength)
