# Read a line of input and remove the trailing newline character
input_line = input().strip()

# Determine the length of the input string
length_of_input = len(input_line)

# Initialize a variable to store the length of the longest repeating substring
longest_repeating_length = 0

# Iterate through possible lengths of substrings starting from 0 up to the length of the input - 1
for substring_length in range(length_of_input):
    # Check every starting index in the string for the given substring length
    for start_index in range(length_of_input):
        # Extract the current substring from the input string
        current_substring = input_line[start_index:start_index + substring_length]

        # If the substring is found again starting from the next index
        if input_line.find(current_substring, start_index + 1) != -1:
            # Update the longest repeating length if a longer substring is found
            longest_repeating_length = substring_length
            break  # Exit the inner loop and check the next substring length

# Output the length of the longest repeating substring
print(longest_repeating_length)
