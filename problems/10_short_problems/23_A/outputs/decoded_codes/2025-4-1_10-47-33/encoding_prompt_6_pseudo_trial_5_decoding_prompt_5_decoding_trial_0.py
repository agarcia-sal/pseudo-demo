# Begin program to find the longest repeating substring length

# Read a line of input and remove the last character (newline).
input_string = input().rstrip()

# Store the length of the input line in a variable called total_length.
total_length = len(input_string)

# Initialize a variable longest_repeat_length to 0 to track the length of the longest repeating substring.
longest_repeat_length = 0

# Loop through possible substring lengths from 0 to total_length
for length in range(total_length + 1):
    # Loop through each starting index from 0 to total_length - length
    for start_index in range(total_length - length + 1):
        # Extract a substring starting from the current index with the current length.
        substring = input_string[start_index:start_index + length]
        
        # Check if this substring appears again in the input, starting from the position after the current index.
        if substring in input_string[start_index + length:]:
            # If found, set longest_repeat_length to the current length.
            longest_repeat_length = length
            
            # Break out of the inner loop as we found a repeating substring of the current length.
            break

# After checking all lengths, output the longest found repeating substring length
print(longest_repeat_length)
