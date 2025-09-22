def find_longest_repeated_substring(input_string):
    # Initialize the length of the input string
    length_of_input = len(input_string)
    longest_repeat_length = 0

    # Loop through potential substring lengths
    for substring_length in range(length_of_input + 1):
        # Check each starting index for the substring
        for start_index in range(length_of_input):
            # Define the current substring
            current_substring = input_string[start_index:start_index + substring_length]

            # Check if the current substring can be found later in the string
            if current_substring in input_string[start_index + 1:]:
                # Update longest_repeat_length if a repeat is found
                longest_repeat_length = substring_length
                break  # Exit the inner loop if a repeat is found

    return longest_repeat_length

# To execute the function:
line = input()[:-1]  # Read user input and remove the last character
print(find_longest_repeated_substring(line))
