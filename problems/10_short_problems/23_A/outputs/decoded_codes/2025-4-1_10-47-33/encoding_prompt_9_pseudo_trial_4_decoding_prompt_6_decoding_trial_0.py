# Start the program

# Step 2: Receive Input
line = input().rstrip()  # Read a line of text and remove any trailing newline character
line_length = len(line)  # Store the length of the line

# Step 3: Initialize Counter
longest_repeated_substring_length = 0  # Variable to track the longest repeated substring length

# Step 4: Iterate Over Possible Substring Lengths
for current_length in range(1, line_length):  # Start from length 1 to line_length - 1
    for start_index in range(line_length - current_length):  # Adjust end range based on current_length
        substring = line[start_index:start_index + current_length]  # Extract the substring
        # Check if substring appears later in the line
        if substring in line[start_index + current_length:]:
            longest_repeated_substring_length = current_length  # Update the length
            break  # Break out of inner loop if a repeated substring is found

# Step 5: Output the Result
print(longest_repeated_substring_length)  # Print the length of the longest repeated substring

# End Program
