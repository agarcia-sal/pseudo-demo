# Read a line of input from the user
line = input()

# Remove the newline character from the end of the input
line = line.strip()

# Calculate the length of the input string
n = len(line)

# Initialize a variable to hold the length of the longest repeated substring
longest_repeated_length = 0

# Loop through substrings of increasing lengths
for length in range(1, n):  # Start from length 1 to n-1 (substrings can't be of length 0)
    
    # Check all starting positions for the substring of the current length
    for start_position in range(n - length + 1):  # Ensuring substring can fit
            
        # Extract the substring from 'start_position' of 'length'
        current_substring = line[start_position:start_position + length]

        # Check if this substring appears again in the string after its starting position
        if line.find(current_substring, start_position + 1) != -1:
            # If the substring is found again, update the longest repeated length
            longest_repeated_length = length
            
            # Exit this inner loop as we found a repeat
            break  

# Print the length of the longest repeated substring found
print(longest_repeated_length)
