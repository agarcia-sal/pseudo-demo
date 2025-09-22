# Step 1: Receive Input
line = input().rstrip()

# Step 2: Initialize Variables
line_length = len(line)
longest_repeated_length = 0

# Step 3: Outer Loop for substring lengths
for substring_length in range(1, line_length):  # Evaluate lengths from 1 to line_length - 1
    # Step 4: Inner Loop for starting positions
    for start_index in range(line_length - substring_length + 1):
        # Extract current substring
        current_substring = line[start_index:start_index + substring_length]
        
        # Step 5: Check for Repetition
        if current_substring in line[start_index + 1:]:
            longest_repeated_length = substring_length
            break  # Exit once a repetition is found
            
# Step 6: Output Result
print(longest_repeated_length)
