# Step 1: Read a line of text input
input_text = input()

# Step 2: Determine the length of the input text
text_length = len(input_text)

# Step 3: Initialize maximumLength to zero
maximum_length = 0

# Step 4: Outer loop to iterate through possible substring lengths
for current_length in range(text_length):
    # Inner loop to iterate through starting positions for substrings
    for start_position in range(text_length):
        # Extract the substring
        substring = input_text[start_position:start_position + current_length]
        
        # Check if the substring exists again in the input text
        if substring in input_text[start_position + 1:]:
            # If a repetition is found, update maximumLength
            maximum_length = current_length
            break # Exit the inner loop to continue with the next substring length

# Step 5: Output the result
print(maximum_length)
