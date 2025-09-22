# Read a line of input from the user
line = input()

# Get the length of the input line
n = len(line)

# Initialize return value
longest_repeating_length = 0

# Iterate over possible substring lengths
for length in range(n):  # from 0 to n-1
    # Check for each starting index in the string
    for start_index in range(n):  # from 0 to n-1
        # Extract the substring of the current length
        substring = line[start_index:start_index + length]
        
        # Check if this substring exists again in the string after the start_index
        if substring in line[start_index + 1:]:  # after start_index
            # Update longest repeating length if found
            longest_repeating_length = length
            break  # Exit inner loop if a repeat is found

# Output the length of the longest repeating substring found
print(longest_repeating_length)
