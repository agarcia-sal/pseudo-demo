# Read the input string and remove the last character
line = input()[:-1]  # We take input and omit the last character

# Determine the length of the input string
n = len(line)
rv = 0  # This will hold the result

# Loop through possible substring lengths from 0 to n-1
for l in range(n):
    # Loop through each starting index of substring
    for i in range(n):
        # Check if the substring of length l starting from index i appears again after index i
        if line.count(line[i:i+l]) > 1:
            rv = l  # If found, update result to current length l
            break  # No need to check further for this length l

# Output the result
print(rv)
