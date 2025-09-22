# Read a line of input and remove the trailing newline character
line = input().strip()

# Determine the length of the input line
n = len(line)

# Initialize a variable to hold the result
repeated_length = 0

# Loop through lengths of substrings from 1 to n-1
for length in range(1, n):
    # Check for substrings of the current length
    for start_index in range(n - length + 1):
        # Extract a substring from the current start index
        substring = line[start_index:start_index + length]
        
        # Check if the substring occurs again later in the string
        if substring in line[start_index + length:]:
            # Update the result with the current length
            repeated_length = length
            break  # Exit inner loop if a repeat is found

# Output the length of the longest repeated substring
print(repeated_length)
