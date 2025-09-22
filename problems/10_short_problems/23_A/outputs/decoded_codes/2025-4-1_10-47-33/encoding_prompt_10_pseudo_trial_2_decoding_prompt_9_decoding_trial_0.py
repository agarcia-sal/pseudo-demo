# Read input
line = input()[:-1]  # Get the input string and omit the last character

# Determine length
n = len(line)
rv = 0  # This will hold the result

# Loop through lengths
for l in range(n):  # For each length from 0 to n-1
    for i in range(n):  # For each starting index from 0 to n-1
        # Check if the substring appears again after index i
        if line[i:i + l] in line[i + 1:]:
            rv = l  # Update the result to current length l
            break  # Exit the inner loop as we found a match

# Output result
print(rv)
