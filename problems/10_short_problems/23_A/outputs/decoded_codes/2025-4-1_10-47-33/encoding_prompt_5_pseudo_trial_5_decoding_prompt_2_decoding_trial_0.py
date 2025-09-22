# Step 1: Read input from the user
input_string = input().rstrip("\n")  # Remove the newline character at the end

# Step 2: Get the length of the input string
length_of_string = len(input_string)
longest_repeated_length = 0

# Step 3: Loop through possible substring lengths
for length in range(0, length_of_string):  # From 0 to length_of_string - 1
    # Step 4: Nested loop to check every position in the string
    for position in range(length_of_string):  # From 0 to length_of_string - 1
        # Step 5: Extract the substring of the current length starting from the current position
        current_substring = input_string[position:position + length + 1]  # Length + 1 for Python slicing
        
        # Step 6: Check if this substring appears again in the string
        if current_substring in input_string[position + 1:]:  # Check in the remaining substring
            # Step 7: Update the longest length if a repeated substring is found
            longest_repeated_length = length + 1  # Update with the actual length
            break  # No need to check further for this length

# Step 8: Output the length of the longest repeated substring found
print(longest_repeated_length)
