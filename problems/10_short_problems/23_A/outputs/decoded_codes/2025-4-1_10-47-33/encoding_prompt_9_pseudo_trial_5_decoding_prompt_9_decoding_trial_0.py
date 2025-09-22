# Get the Input
input_string = input().rstrip()  # Read input and remove trailing newline character
string_length = len(input_string)  # Store the length of the input string
longest_repeated_substring_length = 0  # Initialize the tracker for the longest length

# Iterate Over Possible Substring Lengths
for current_length in range(1, string_length):  # Start from 1 to ensure substring has length
    for start_position in range(string_length - current_length + 1):  # Ensure we don't go out of bounds
        # Extract the substring from the current start position
        substring = input_string[start_position:start_position + current_length]
        
        # Check if this substring appears again in the remainder of the string
        if substring in input_string[start_position + 1:]:  # Search in the string after the current position
            longest_repeated_substring_length = current_length  # Update the maximum length found
            break  # Exit the inner loop if a repeated substring is found

# Output the Length
print(longest_repeated_substring_length)  # Print the length of the longest repeated substring
