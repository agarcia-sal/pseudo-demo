# Start of the program

# Step 2: Receive Input
text_line = input().strip()  # Read a line of text
text_length = len(text_line)  # Store the length of the line
longest_repeated_length = 0  # Initialize the longest repeated length

# Step 3: Loop through Substring Lengths
for current_length in range(1, text_length):  # Start from 1 to avoid empty substrings
    for current_index in range(text_length - current_length + 1):  # Ensure we don't go out of bounds
        substring = text_line[current_index:current_index + current_length]  # Extract substring
        
        # Check if this substring occurs again in the line after current_index
        if substring in text_line[current_index + current_length:]:
            longest_repeated_length = current_length  # Update the longest repeated length
            break  # Found a match, no need to check further in this length

# Step 4: Output Result
print(longest_repeated_length)  # Print the length of the longest repeated substring

# End of the program
