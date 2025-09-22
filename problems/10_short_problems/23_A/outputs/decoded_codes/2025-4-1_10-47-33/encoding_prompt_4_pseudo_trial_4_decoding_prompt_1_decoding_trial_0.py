# BEGIN

# Read a line of input and remove the trailing newline character
line = input()
n = len(line)
longest_repeated_length = 0

# Iterate through possible lengths of substrings
for length in range(n):  # From 0 to n-1
    # Check for repeated substrings of the current length
    for start_index in range(n):  # From 0 to n-1
        # Extract the substring
        substring = line[start_index:start_index + length]
        
        # Check if the substring occurs again after the current index
        if substring in line[start_index + 1:]:
            longest_repeated_length = length
            break  # Break out of the inner loop
            
# Output the length of the longest repeated substring
print(longest_repeated_length)

# END
