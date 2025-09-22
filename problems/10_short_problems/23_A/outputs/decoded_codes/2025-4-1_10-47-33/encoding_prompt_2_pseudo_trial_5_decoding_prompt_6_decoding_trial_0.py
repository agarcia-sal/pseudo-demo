# Step 1: Read a single line of input and remove the newline character
input_string = input().strip()

# Step 2: Determine the length of input_string
length_of_input_string = len(input_string)

# Step 3: Initialize variable to track the longest repeated substring length
longest_repeated_substring_length = 0

# Step 4: Loop through each possible length of substrings
for current_length in range(1, length_of_input_string):
    # Step 5: For each starting position in input_string
    for start_position in range(length_of_input_string - current_length):
        # Step 6: Extract the substring
        substring = input_string[start_position:start_position + current_length]
        
        # Step 7: Check for repeated occurrence in input_string
        if substring in input_string[start_position + current_length:]:
            # Step 8: Update longest_repeated_substring_length
            longest_repeated_substring_length = current_length
            break  # Found a repeated substring, break the inner loop

# Step 9: Continue with the outer loop until all lengths have been checked

# Step 10: Output the result
print(longest_repeated_substring_length)
