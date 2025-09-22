# BEGIN

# Read a line of input and remove the trailing newline character
line = input().strip()  # Read input and remove any new line
n = len(line)            # Set n to the length of the line
longest_repeated_length = 0  # Initialize longest repeated length to 0

# Iterate through possible lengths of substrings
for length in range(n):  # Length can vary from 0 to n-1
    # Check for repeated substrings of the current length
    for start_index in range(n):  # Start index can vary from 0 to n-1
        # Extract the substring
        substring = line[start_index:start_index + length]
        
        # Check if the substring occurs again after the current index
        if substring in line[start_index + 1:]:  # Check for occurrence after start_index
            longest_repeated_length = length  # Update the longest repeated length
            break  # Break out of inner loop
    # The outer loop will continue to the next length

# Output the length of the longest repeated substring
print(longest_repeated_length)

# END
