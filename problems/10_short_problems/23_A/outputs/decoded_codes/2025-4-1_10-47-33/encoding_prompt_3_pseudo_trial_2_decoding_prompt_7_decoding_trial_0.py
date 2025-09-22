# This program finds the length of the longest repeated substring in a given string.

# Read a line of input
line = input().strip()  # Read input and remove trailing newline
n = len(line)            # Get the length of the input string
repeatedLength = 0       # This variable will hold the length of the longest repeated substring

# Loop through possible lengths of substrings starting from 0 to n-1
for possibleLength in range(n):  # possibleLength will take values from 0 to n-1
    # Inner loop to evaluate each starting position for substrings of the current possibleLength
    for index in range(n - possibleLength):  # prevents index out of range for substring
        # Extract a substring of length possibleLength starting from the current index
        substring = line[index:index + possibleLength]

        # Check if this substring appears later in the line
        if substring in line[index + 1:]:  # Check if the substring appears after the current index
            repeatedLength = possibleLength  # Update the length of the repeated substring
            break  # Exit the inner loop as we found a repeated substring

# Output the length of the longest repeated substring found
print(repeatedLength)
