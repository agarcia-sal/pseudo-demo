# Start Program

# Accept Input
line = input()  # Read a line of text from the user
line = line.strip()  # Remove trailing newline or whitespace characters
n = len(line)  # Get the length of the input string

# Initialize Variables
maximum_length = 0  # Set variable to keep track of the maximum length

# Loop Through Possible Substring Lengths
for l in range(n):  # For each length from 0 to n-1
    # Inner Loop to Check Substrings
    for i in range(n - l):  # For each starting position of the substring
        substring = line[i:i + l]  # Extract substring of the current length
        
        # Check if this substring can be found later in the string
        if substring in line[i + 1:]:  # Check if substring found in the rest of the line
            maximum_length = l  # Update the maximum_length variable
            break  # Stop searching further; break out of the inner loop

# Output Result
print(maximum_length)  # Print the maximum length of the repeating substring
