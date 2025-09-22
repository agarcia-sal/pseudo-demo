# Begin program to find the longest repeating substring length

# Step 1: Read a line of input and remove the last character (newline).
input_line = input().rstrip()

# Step 2: Store the length of the input line in a variable called total_length.
total_length = len(input_line)

# Step 3: Initialize a variable longest_repeat_length to 0 to track the length of the longest repeating substring.
longest_repeat_length = 0

# Step 4: Loop through possible substring lengths from 1 to total_length (inclusive).
for current_length in range(1, total_length + 1):
    # Step 4a: Loop through each starting index from 0 to total_length - current_length (inclusive).
    for start_index in range(total_length - current_length + 1):
        # Step 4ai: Extract a substring starting from the current index with the current length.
        substring = input_line[start_index:start_index + current_length]
        
        # Step 4aii: Check if this substring appears again in the input, starting from the position after the current index.
        if input_line.find(substring, start_index + current_length) != -1:
            # Step 4aiii: If found, set longest_repeat_length to the current length.
            longest_repeat_length = current_length
            
            # Step 4aiv: Break out of the inner loop as we found a repeating substring of the current length.
            break

# Step 5: Print longest_repeat_length
print(longest_repeat_length)
