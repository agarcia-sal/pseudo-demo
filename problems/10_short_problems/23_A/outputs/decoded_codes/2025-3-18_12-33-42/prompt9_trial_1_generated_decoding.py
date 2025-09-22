# Read input string from the user
user_input_string = input()

# Calculate the length of the input string
string_length = len(user_input_string)

# Initialize a variable to store the maximum length of duplicating substring
longest_duplicate_length = 0

# Loop through possible lengths of substrings
for substring_length in range(1, string_length):  # Start from 1 to avoid empty substring
    # Loop through each starting index for the substring
    for starting_index in range(string_length - substring_length + 1):  # Ensure we don't exceed bounds
        
        # Extract the current substring
        current_substring = user_input_string[starting_index:starting_index + substring_length]
        
        # Check if the current substring occurs later in the string
        if current_substring in user_input_string[starting_index + 1:]:  # Check from the next index onward
            # Update the longest duplicate length if a longer duplicate is found
            longest_duplicate_length = substring_length
            
            # Exit the inner loop as we found a valid duplicate
            break
    
# Output the length of the longest duplicate substring found
print(longest_duplicate_length)
