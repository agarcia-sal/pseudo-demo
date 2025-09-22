def find_longest_repeated_substring(input_string):
    # Initialize the length of the input string
    length_of_input = len(input_string)
    # Initialize variable to store the longest repeated substring length
    longest_repeat_length = 0

    # Loop over possible substring lengths
    for substring_length in range(length_of_input):
        # Loop over possible starting indices for substrings
        for start_index in range(length_of_input):
            # Define the current substring from the input string
            current_substring = input_string[start_index:start_index + substring_length]

            # Check if the current substring can be found later in the input string
            if current_substring in input_string[start_index + 1:]:
                # Update the longest repeated substring length
                longest_repeat_length = substring_length
                break  # Found a repeat, we can break out of the inner loop

    # Return the length of the longest repeated substring found
    return longest_repeat_length

# Read input string without the last character
line = input()[:-1]
# Output the result of the function
print(find_longest_repeated_substring(line))
