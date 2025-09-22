# Start Program

# Input: Read a line of text from the standard input, excluding the last character
text = input()[:-1]  # Exclude the last character (newline)
text_length = len(text)  # Determine the length of the input text

# Initialize a variable
resultValue = 0  # Keeps track of the longest valid substring length

# Outer Loop: For each possible length "l"
for l in range(text_length + 1):  # from 0 to the length of the text
    # Inner Loop: For each starting position "i"
    for i in range(text_length):
        # Extract a substring from the text that starts at index "i" and extends for "l" characters
        substring = text[i:i + l]

        # Check for Substring Existence
        if substring in text[i + 1:]:  # Look for the same substring starting from index "i + 1"
            resultValue = l  # Set "resultValue" to the current length "l"
            break  # Break out of the inner loop

# Output: Display or print the value of "resultValue"
print(resultValue)  # This indicates the length of the longest valid substring found

# End Program
