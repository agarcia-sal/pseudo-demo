# Function to find the length of the longest repeating substring in a given line of text
def longest_repeating_substring():
    # Read a line of text, removing the newline character
    line_of_text = input().strip()
    
    # Determine the length of the line of text
    text_length = len(line_of_text)
    
    # Initialize the maximum length of repeating substring to zero
    maximum_length = 0
    
    # Outer loop: for each possible length of substring from 1 to text_length
    for current_length in range(1, text_length):
        # Inner loop: for each starting position in the line
        for start_position in range(text_length - current_length):
            # Extract the substring of current_length starting from start_position
            substring = line_of_text[start_position:start_position + current_length]
            # Check if this substring appears again after its position
            if substring in line_of_text[start_position + current_length:]:
                # Update maximum length to current_length
                maximum_length = current_length
                # Exit the inner loop as we found a valid repetition
                break
    
    # Output the maximum length of repeating substring found
    print(maximum_length)

# You may include test cases as comments for validation purposes
# Example test case:
# Input: "abcabc"
# Output: 3 (the substring "abc" repeats)
