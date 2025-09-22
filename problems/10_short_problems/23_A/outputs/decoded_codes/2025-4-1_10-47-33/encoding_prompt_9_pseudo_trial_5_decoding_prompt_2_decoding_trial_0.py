# Step 1: Get the Input
input_string = input().rstrip()  # Read a line of text and remove trailing newline character
string_length = len(input_string)  # Store the length of the input string
longest_repeated_substring_length = 0  # Initialize the maximum length of the repeated substring found

# Step 2: Iterate Over Possible Substring Lengths
for current_length in range(1, string_length):  # For each possible substring length from 1 to string_length - 1
    for start_position in range(string_length - current_length + 1):  # Starting position must ensure a full substring
        substring = input_string[start_position:start_position + current_length]  # Extract the substring
        remaining_string = input_string[start_position + 1:]  # Get the rest of the string after current starting position
        
        # Check if the substring appears again in the remaining string
        if substring in remaining_string:
            longest_repeated_substring_length = current_length  # Update max length found
            break  # Exit the inner loop since we found a repeated substring

# Step 3: Output the Length
print(longest_repeated_substring_length)  # Print the length of the longest repeated substring
