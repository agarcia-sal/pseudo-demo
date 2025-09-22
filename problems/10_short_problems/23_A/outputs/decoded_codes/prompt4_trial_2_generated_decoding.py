# Read a line of input
line = input().rstrip('\n')

# Determine the length of the input line
n = len(line)
rv = 0  # Initialize a variable to store the result

# Loop through each possible length of substring
for l in range(n):
    # Check for substrings of the current length
    for i in range(n):
        # Ensure we don't go out of bounds
        if i + l < n:
            # Check if the substring from index i of length l exists further in the line
            substring = line[i:i + l + 1]
            if substring in line[i + 1:]:
                # Update the result to the current length l
                rv = l
                break
    else:
        # If we completed the inner loop without `break`, we can skip checking further lengths
        continue
    # If we reached here, we broke out of the inner loop
    break

# Output the result
print(rv)
