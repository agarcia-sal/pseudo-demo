# Purpose: To find the length of the longest substring that appears more than once in the given input string.

# Step 1: Start Program

# Step 2: Receive Input
input_string = input()  # Read a line of text from the user
if input_string.endswith("\n"):  # Check if there's a newline at the end and remove it.
    input_string = input_string[:-1]

length_of_string = len(input_string)  # Store the length of the string
longest_repeated_substring_length = 0  # Initialize variable for the longest repeated substring length

# Step 3: Loop Through Substring Lengths
for current_length in range(length_of_string):  # Loop from 0 to length_of_string - 1
    for start_index in range(length_of_string):  # Loop through each starting index
        if start_index + current_length <= length_of_string:  # Ensure substring does not exceed bounds
            substring = input_string[start_index:start_index + current_length]  # Extract substring

            # Check if this substring occurs again in the string after starting index
            if substring in input_string[start_index + current_length:]:
                longest_repeated_substring_length = current_length  # Update longest length if repeated
                break  # Break, as we only need the longest first occurrence

# Step 4: Output Result
print(longest_repeated_substring_length)  # Print the length of the longest repeated substring

# Step 5: End Program
