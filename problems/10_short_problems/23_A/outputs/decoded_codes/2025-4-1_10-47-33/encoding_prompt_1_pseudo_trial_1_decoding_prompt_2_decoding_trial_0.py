input_line = input().strip()  # Read input and remove trailing newline
length_of_input = len(input_line)  # Determine the length of the input
longest_repeated_substring_length = 0  # Initialize the longest repeated substring length


for current_length in range(length_of_input):  # Loop current length from 0 to length_of_input - 1


    for start_index in range(length_of_input):  # Loop over each starting index
        current_substring = input_line[start_index:start_index + current_length]  # Extract substring

        # Check for existence of current_substring after the current starting index
        if current_substring in input_line[start_index + 1:]:


            longest_repeated_substring_length = current_length  # Update the length
            break  # Exit the inner loop to check the next current_length


print(longest_repeated_substring_length)  # Output the result


input_line = input().strip()  # Read input and remove trailing newline
length_of_input = len(input_line)  # Determine the length of the input
longest_repeated_substring_length = 0  # Initialize the longest repeated substring length

for current_length in range(length_of_input):  # Loop current length from 0 to length_of_input - 1
    for start_index in range(length_of_input):  # Loop over each starting index
        current_substring = input_line[start_index:start_index + current_length]  # Extract substring
        if current_substring in input_line[start_index + 1:]:  # Check for existence of current_substring after the current starting index
            longest_repeated_substring_length = current_length  # Update the length
            break  # Exit the inner loop to check the next current_length

print(longest_repeated_substring_length)  # Output the result
