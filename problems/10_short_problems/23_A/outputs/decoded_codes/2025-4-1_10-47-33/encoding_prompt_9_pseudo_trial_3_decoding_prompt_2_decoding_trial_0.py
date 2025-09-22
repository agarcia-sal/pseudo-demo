# 1. Start Program

# 2. Receive Input
input_string = input()  # Read a line of text from the user (input string)
input_string = input_string.rstrip('\n')  # Remove the last character if it is a newline
length_of_string = len(input_string)  # Store the length of the string
longest_repeated_substring_length = 0  # Initialize variable to zero

# 3. Loop Through Substring Lengths
for current_length in range(length_of_string):  # For each possible length from 0 to length_of_string - 1
    for start_index in range(length_of_string):  # Loop through each starting index
        # Check if the substring can be created (it must fit within the length of the string)
        if start_index + current_length <= length_of_string:
            substring = input_string[start_index:start_index + current_length]  # Extract the substring
            # Check if the substring occurs again in the string
            if substring in input_string[start_index + 1:]:  # Check after the current index
                longest_repeated_substring_length = current_length  # Update the longest found
                break  # Break out of the inner loop to check for longer lengths

# 4. Output Result
print(longest_repeated_substring_length)  # Print the value of longest_repeated_substring_length

# 5. End Program
