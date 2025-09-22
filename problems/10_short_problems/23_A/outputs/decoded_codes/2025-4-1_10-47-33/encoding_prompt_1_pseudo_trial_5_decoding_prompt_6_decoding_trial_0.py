# Step 1: Read input and remove trailing newline
line = input().strip()

# Step 2: Store the length of the input line
length_of_line = len(line)

# Step 3: Initialize maximum repeated length
max_repeated_length = 0

# Step 4: Outer loop for current length of substrings
for current_length in range(length_of_line):
    # Inner loop for starting index of the substring
    for start_index in range(length_of_line):
        # Extract the substring from the line
        substring = line[start_index:start_index + current_length]
        
        # Check if the substring appears again in the line
        if substring in line[start_index + 1:]:
            # Update maximum repeated length
            max_repeated_length = current_length
            break  # Break the inner loop if we found a repeat

# Step 5: Output the result
print(max_repeated_length)
