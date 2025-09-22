# Read a line of input and remove the trailing newline
line = input().strip()
n = len(line)
repeatedLength = 0  # This variable will hold the length of the repeated substring

# Loop through possible lengths of substrings starting from 0 to n-1
for possibleLength in range(n):
    # Inner loop to evaluate each starting position for substrings of the current possibleLength
    for index in range(n):
        # Extract a substring of length possibleLength starting from the current index
        substring = line[index:index + possibleLength]

        # Check if this substring appears later in the line
        if substring in line[index + 1:]:
            repeatedLength = possibleLength
            break  # Exit inner loop as we found a repeated substring

# Output the length of the longest repeated substring found
print(repeatedLength)
