# Start Program

# Accept Input
line = input().rstrip()  # Read a line of text and remove trailing whitespace and newline
n = len(line)  # Get the length of the input string

# Initialize Variables
maximum_length = 0  # Variable to track the maximum length of repeating substring

# Loop Through Possible Substring Lengths
for l in range(n):  # For each length l from 0 to n-1
    for i in range(n - l):  # For each starting position i from 0 to n-l
        substring = line[i:i + l]  # Extract substring from index i of length l
        # Check if this substring can be found later in the string
        if substring in line[i + 1:]:  # If substring can be found in line starting from index i+1
            maximum_length = l  # Update maximum length
            break  # Exit the inner loop

# Output Result
print(maximum_length)  # Print the maximum length of the repeating substring
