# Read Input
line = input()[:-1]  # Omitting the last character

# Determine Length
n = len(line)
rv = 0  # This will hold the result

# Loop Through Lengths
for l in range(n):  # l ranges from 0 to n-1
    for i in range(n):  # i ranges from 0 to n-1
        # Check if the substring from index i of length l appears again in line
        if line[i:i + l] in line[i + 1:]:
            rv = l  # Update rv to the current length l
            break  # Exit the inner loop as we found a match

# Output Result
print(rv)
