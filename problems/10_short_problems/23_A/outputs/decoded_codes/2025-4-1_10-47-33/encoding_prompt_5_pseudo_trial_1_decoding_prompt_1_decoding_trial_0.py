# Start Program

# Accept Input
line = input().rstrip()  # Read text input and remove trailing whitespace
n = len(line)  # Get length of input

# Initialize Variables
maximum_length = 0  # Variable to keep track of maximum length of repeating substring

# Loop Through Possible Substring Lengths
for l in range(n):  # For each length l from 0 to n-1
    for i in range(n - l):  # For each starting position i from 0 to n-l
        substring = line[i:i + l]  # Get substring from index i of length l
        if substring in line[i + 1:]:  # Check if this substring can be found later in the string
            maximum_length = l  # Update maximum_length to l
            break  # Exit inner loop (move to next length l)

# Output Result
print(maximum_length)  # Print maximum_length

# End Program
