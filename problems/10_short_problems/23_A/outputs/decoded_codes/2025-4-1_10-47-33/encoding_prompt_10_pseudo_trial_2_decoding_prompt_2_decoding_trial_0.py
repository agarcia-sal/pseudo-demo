# Read Input
line = input()[:-1]  # Set variable `line` to the input string received, omitting the last character

# Determine Length
n = len(line)  # Set variable `n` to the length of `line`
rv = 0  # Set variable `rv` to 0 (this will hold the result)

# Loop Through Lengths
for l in range(n):  # For each integer `l` from 0 to `n - 1` (inclusive)
    for i in range(n):  # For each integer `i` from 0 to `n - 1` (inclusive)
        # Check if the substring from `line` starting at index `i` with length `l` appears again
        substring = line[i:i+l]  # Get the substring of length `l` starting at index `i`
        if substring in line[i+1:]:  # Check if this substring appears after index `i`
            rv = l  # Set `rv` to `l`
            break  # Exit the inner loop

# Output Result
print(rv)  # Print the value of `rv`
