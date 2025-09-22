# Read a line of input from the user
line = input()
line = line[:-1]  # Remove the last character (newline)

# Determine the length of the input line
n = len(line)
rv = 0  # Initialize the result variable

# Loop through all possible lengths of substrings from 0 to n-1
for l in range(n):
    # Loop through the starting index of the substring
    for i in range(n):
        # Check if the substring from index i to i+l exists later in the string
        substring = line[i:i+l+1]
        if line.find(substring, i + 1) != -1:
            rv = l  # Update result variable with current length l
            break  # Exit the inner loop
    else:
        continue  # This "else" corresponds to the inner for-loop
    break  # If we hit a break in the inner loop, we also want to break the outer one

# Print the result variable indicating the length of the substring found
print(rv)
