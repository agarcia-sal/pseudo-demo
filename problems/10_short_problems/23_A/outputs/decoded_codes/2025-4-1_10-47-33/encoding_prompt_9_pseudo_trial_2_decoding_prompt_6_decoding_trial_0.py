# Step 1: Read Input
input_string = input()  # User inputs a string of characters
string_length = len(input_string)  # Calculate the length of the input string
longest_repeating_substring_length = 0  # Initialize variable to hold the length of the longest repeating substring

# Step 2: Iterate through substring lengths
for current_length in range(1, string_length):  # Start from length 1 to string_length - 1
    for start_index in range(string_length - current_length):  # Ensure we don't go out of bounds
        # Step 2.1: Extract Substring
        substring = input_string[start_index:start_index + current_length]  # Get the substring
        
        # Step 2.2: Search for Repeats
        if substring in input_string[start_index + current_length:]:  # Look for repeats in the remaining string
            longest_repeating_substring_length = current_length  # Update the longest length found
            break  # Exit the inner loop as we found a repeating substring for this length

# Step 3: Output Result
print(longest_repeating_substring_length)  # Print the length of the longest repeated substring
