# Start Program

# Accept Input
line = input()
line = line.rstrip()  # Remove trailing newline or whitespace
n = len(line)  # Length of the input string

# Initialize Variables
maximum_length = 0

# Loop Through Possible Substring Lengths
for l in range(1, n):  # Start from 1 to ensure we have non-empty substrings
    for i in range(n - l + 1):
        substring = line[i:i + l]  # Get substring of length l starting at index i
        if substring in line[i + 1:]:  # Check if substring occurs again later in the string
            maximum_length = l  # Update maximum length
            break  # Exit inner loop and move to the next length

# Output Result
print(maximum_length)

# End Program
