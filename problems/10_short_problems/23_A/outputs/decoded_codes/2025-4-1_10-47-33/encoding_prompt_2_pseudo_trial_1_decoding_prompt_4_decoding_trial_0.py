# Read input
user_input = input().strip()

# Determine length
string_length = len(user_input)

# Initialize variable for longest repeated substring length
repeated_substring_length = 0

# Outer loop: Iterate over substring lengths
for substring_length in range(1, string_length):  # Start from 1 since a length of 0 is not meaningful
    # Inner loop: Iterate over possible starting indices
    for start_index in range(string_length - substring_length + 1):
        # Extract the substring
        substring = user_input[start_index:start_index + substring_length]
        
        # Check if this substring appears later in the string
        if substring in user_input[start_index + substring_length:]:
            # Update the length of the longest repeated substring
            repeated_substring_length = substring_length
            break  # Exit inner loop once we find at least one repeat

# Output the result
print(repeated_substring_length)
