# Read input and initialize variables
line = input()  # Read a line of input from standard input
line = line[:-1]  # Remove the last character from line
n = len(line)  # Get the length of the line
rv = 0  # This variable stores the result

# Iterate through lengths l from 0 to n-1
for l in range(n):  # l goes from 0 to n-1
    # Iterate through each starting index i from 0 to n-1
    for i in range(n):  # i goes from 0 to n-1
        # Check if the substring exists later in the string
        if line[i:i+l+1] in line[i+1:]:  # Adjust the slice to include l characters
            rv = l + 1  # Update rv with the current length (adding 1 because l is 0-indexed)
            break  # Exit the inner loop as the substring is found

# Output the result
print(rv)  # Display the final value of rv
