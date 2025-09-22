# Read a string of characters from the user
input_string = input().strip()  # Strip any trailing whitespace or newline
string_length = len(input_string)  # Get the length of the string
longest_repeated_substring_length = 0  # Initialize the length of the longest repeated substring

# Begin loop through possible substring lengths
for substring_length in range(1, string_length):  # start from 1 to avoid length 0
    for start_index in range(string_length - substring_length):  # prevent index overflow
        substring = input_string[start_index:start_index + substring_length]  # Extract the substring
        
        # Check if this substring appears again in the original string
        if substring in input_string[start_index + substring_length:]:  # search after the current position
            longest_repeated_substring_length = substring_length  # Update the longest found length
            break  # Exit the inner loop since we only need the longest length

# Output the result
print(longest_repeated_substring_length)  # Print the length of the longest repeated substring
