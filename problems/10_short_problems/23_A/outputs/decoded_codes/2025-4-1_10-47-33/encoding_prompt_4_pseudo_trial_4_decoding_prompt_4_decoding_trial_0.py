# Read a line of input and remove any trailing newline characters
line = input().strip()
n = len(line)
longest_repeated_length = 0

# Iterate through possible lengths of substrings
for length in range(1, n):  # Starting from 1 since length 0 has no substrings
    # Check for repeated substrings of the current length
    for start_index in range(n - length):
        # Extract the substring
        substring = line[start_index:start_index + length]

        # Check if the substring occurs again after the current index
        if substring in line[start_index + length:]:
            longest_repeated_length = length
            break  # Found a repeated substring, no need to check further for this length

# Output the length of the longest repeated substring
print(longest_repeated_length)
