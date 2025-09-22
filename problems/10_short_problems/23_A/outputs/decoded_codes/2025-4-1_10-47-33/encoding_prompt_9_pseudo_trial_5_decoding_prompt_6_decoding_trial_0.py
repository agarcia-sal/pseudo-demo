# Step 1: Get the input string from the user
input_string = input().strip()  # Read a line and remove trailing newline characters
string_length = len(input_string)  # Store the length of the input string

# Step 2: Initialize a variable to track the longest repeated substring length
longest_repeated_substring_length = 0  # Start with 0 since we haven't found any repeated substrings yet

# Step 3: Iterate over possible substring lengths
for current_length in range(1, string_length):  # Start from 1 since a length of 0 is not meaningful
    for start_position in range(string_length - current_length + 1):  # Ensure we don't go out of bounds
        # Step 4: Extract the substring
        substring = input_string[start_position:start_position + current_length]

        # Step 5: Check for the presence of this substring in the rest of the string
        if substring in input_string[start_position + 1:]:
            longest_repeated_substring_length = current_length  # Update the length if found
            break  # Exit the inner loop once we find a repeated substring

# Step 6: Output the length of the longest repeated substring
print(longest_repeated_substring_length)
