# 1. Get the Input
input_string = input().strip()  # Read a line of text from user input and remove trailing newlines
string_length = len(input_string)  # Store the length of the input string
longest_repeated_substring_length = 0  # Initialize to track max length of repeated substring found

# 2. Iterate Over Possible Substring Lengths
for current_length in range(1, string_length):  # Loop from 1 to string_length - 1
    for start_position in range(string_length):  # Loop from 0 to string_length - 1
        if start_position + current_length <= string_length:  # Ensure the substring is within bounds
            substring = input_string[start_position:start_position + current_length]  # Extract substring
            # Check if the substring appears again in the remainder of the string
            if substring in input_string[start_position + 1:]:  # Search for the substring in the remaining string
                longest_repeated_substring_length = current_length  # Update longest length found
                break  # Exit inner loop if a repeated substring is found

# 3. Output the Length
print(longest_repeated_substring_length)  # Print the length of the longest repeated substring
