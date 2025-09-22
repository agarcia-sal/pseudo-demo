# Receive input and remove the last character
input_string = input().strip()

# Initialize variables
total_length = len(input_string)
longest_repeated_length = 0

# Loop through substring lengths
for current_length in range(total_length):
    # Flag to check if we found a repeated substring
    found_repeated = False
    
    # Check for repeated substrings
    for current_position in range(total_length - current_length):
        # Extract the substring
        substring = input_string[current_position:current_position + current_length + 1]
        
        # Search for this substring in the remaining portion of the string
        if substring in input_string[current_position + 1:]:
            longest_repeated_length = current_length + 1  # Update length
            found_repeated = True  # Mark that we found a repeated substring
            break  # No need to check further, break the inner loop
            
    # If we found a repeated substring of this length, no need to look for longer lengths
    if found_repeated:
        continue

# Output result
print(longest_repeated_length)
