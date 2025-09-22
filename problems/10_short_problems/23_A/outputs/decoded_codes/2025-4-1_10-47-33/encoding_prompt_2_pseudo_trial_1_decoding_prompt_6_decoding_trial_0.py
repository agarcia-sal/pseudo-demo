# Step 1: Read input from the user
input_string = input().strip()  # Taking input and removing any trailing newline character

# Step 2: Calculate the length of the input string
string_length = len(input_string)  # Getting the length of the input string

# Step 3: Initialize variable to track length of the longest repeated substring
repeated_substring_length = 0  # Starting with zero as no substring has been found yet

# Step 4: Loop through all possible substring lengths
for substring_length in range(1, string_length):  # Start from 1 to string_length - 1
    # Step 4a: Loop through all possible starting indices
    for start_index in range(string_length - substring_length + 1):
        # Extract the substring of the current length
        current_substring = input_string[start_index:start_index + substring_length]
        
        # Check if the substring appears again in the rest of the string
        if current_substring in input_string[start_index + substring_length:]:
            # Update the length of the longest repeated substring
            repeated_substring_length = substring_length
            break  # Exit the inner loop since a repeat has been found

# Step 5: Output the result
print(repeated_substring_length)  # Display the length of the longest repeated substring found
