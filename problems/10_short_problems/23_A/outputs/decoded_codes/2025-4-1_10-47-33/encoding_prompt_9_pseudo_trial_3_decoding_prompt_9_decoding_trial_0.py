# Start Program

# Receive Input
input_string = input()  # Read a line of text from the user
input_string = input_string.rstrip('\n')  # Remove the last character if it's a newline
length_of_string = len(input_string)  # Store the length of the string
longest_repeated_substring_length = 0  # Initialize longest repeated substring length

# Loop Through Substring Lengths
for current_length in range(length_of_string):  # For each possible length from 0 to length_of_string - 1
    for start_index in range(length_of_string - current_length):  # Loop through each starting index
        substring = input_string[start_index:start_index + current_length]  # Extract the substring
        # Check if this substring occurs again in the string
        if substring in input_string[start_index + current_length:]:
            longest_repeated_substring_length = current_length  # Update the longest length
            break  # Break out of the current loop as we found a repeated substring

# Output Result
print(longest_repeated_substring_length)  # Print the length of the longest repeated substring

# End Program
