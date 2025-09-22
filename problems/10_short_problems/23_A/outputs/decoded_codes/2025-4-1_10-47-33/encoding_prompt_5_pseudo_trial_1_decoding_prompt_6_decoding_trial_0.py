# Start Program

# Accept Input: Read a line of text from the user
input_string = input().strip()  # Removing trailing newline or whitespace characters
n = len(input_string)  # Determine the length of this input string

# Initialize Variables: maximum_length to keep track of the maximum length of the repeating substring
maximum_length = 0

# Loop Through Possible Substring Lengths
for length in range(n):  # From 0 to n-1
    for start in range(n - length):  # From 0 to n - length
        # Get the current substring
        substring = input_string[start:start + length]  # Extract substring
        
        # Check if this substring can be found later in the string
        if substring in input_string[start + 1:]:  # Search in the rest of the string after the current start
            maximum_length = length  # Update the maximum_length
            break  # Exit inner loop to check next length

# Output Result: Print the maximum length of the repeating substring that is found
print(maximum_length)
