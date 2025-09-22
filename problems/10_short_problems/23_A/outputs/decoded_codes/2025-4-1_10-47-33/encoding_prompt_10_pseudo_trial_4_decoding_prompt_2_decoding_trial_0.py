# Begin the program

# Read a line of input from the user
line = input().rstrip()  # Remove the last character (newline)

# Determine the length of the input line
n = len(line)
rv = 0  # Initialize the result variable

# Loop through all possible lengths of substrings from 0 to n-1
for l in range(n):
    # Loop through the starting index of the substring
    for i in range(n):
        # Get the substring from index i to i+l
        substring = line[i:i+l+1]
        # Check if the substring exists later in the string
        if line.find(substring, i + 1) != -1:
            rv = l  # Update result variable with current length l
            break  # Exit the inner loop
    # Optional: Break the outer loop if we have found a matching substring length
    if rv == l:
        break

# Print the result variable indicating the length of the substring found
print(rv)

# End the program
