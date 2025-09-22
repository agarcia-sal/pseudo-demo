def find_longest_repeated_substring(line):
    n = len(line)
    longest_repeated_length = 0

    # Check all possible substring lengths
    for length in range(1, n):  # Length should start from 1 not 0
        for start_index in range(n - length):
            substring = line[start_index:start_index + length]
            # Check if the substring is found again in the rest of the string
            if substring in line[start_index + length:]:
                longest_repeated_length = length
                break  # Found a repeated substring, break inner loop

    return longest_repeated_length

# Read input line and remove trailing newline
input_line = input().strip()
result = find_longest_repeated_substring(input_line)
print(result)
