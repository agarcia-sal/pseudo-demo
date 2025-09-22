# Read input
line = input()[:-1]  # Read input and omit the last character

# Determine length
n = len(line)
rv = 0  # This variable will hold the result

# Loop through possible substring lengths
for l in range(n):
    for i in range(n):
        # Check if the substring from `line` that starts at index `i` and has length `l`
        # appears again in `line` starting after index `i`
        if line[i:i+l] in line[i+1:]:
            rv = l  # Update the result with the found length
            break  # Exit the inner loop as no further checks are needed for this length

# Output the result
print(rv)
