# Read a line of text from the user
line_of_text = input()

# Determine the length of the line of text
text_length = len(line_of_text)

# Initialize a variable to keep track of the longest repeating substring found
maximum_length = 0

# Outer Loop: Check each possible length of substring
for current_length in range(1, text_length):  # Start from 1 to avoid empty substrings
    # Inner Loop: Check each starting position of the substring
    for start_position in range(text_length - current_length + 1):
        # Extract the substring
        substring = line_of_text[start_position:start_position + current_length]
        
        # Check if this substring appears again in the line
        if substring in line_of_text[start_position + 1:]:
            maximum_length = current_length  # Update maximum_length
            break  # Exit inner loop since we found a repeat for this length

# Output the length of the longest repeating substring found
print(maximum_length)
