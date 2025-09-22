# Read input string from user
input_string = input().strip()  # Remove any trailing newline character
string_length = len(input_string)  # Calculate the length of the string
longest_prefix_length = 0  # Initialize variable for the result

# Outer loop for prefix length
for current_prefix_length in range(string_length):  # From 0 to string_length - 1
    # Inner loop for starting position to search for the substring
    for starting_index in range(string_length):  # From 0 to string_length - 1
        # Extract substring from input_string
        substring = input_string[starting_index:starting_index + current_prefix_length]
        
        # Check if this substring appears again in input_string starting from index + 1
        if substring in input_string[starting_index + 1:]:
            longest_prefix_length = current_prefix_length  # Update the longest prefix length
            break  # Exit inner loop since we found a match

# Output the result
print(longest_prefix_length)
