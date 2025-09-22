# Read a line of input and remove trailing newlines
line = input().strip()
n = len(line)
repeated_length = 0  # This variable will hold the length of the repeated substring

# Loop through possible lengths of substrings from 0 to n-1
for possible_length in range(n):
    # Inner loop to evaluate each starting position for substrings of the current possible_length
    for index in range(n):
        # Extract a substring of length possible_length starting from the current index
        substring = line[index:index + possible_length]

        # Check if this substring appears later in the line
        if substring in line[index + 1:]:
            repeated_length = possible_length  # Update the length of the longest found repeated substring
            break  # Exit inner loop as we found a repeated substring

# Output the length of the longest repeated substring found
print(repeated_length)
