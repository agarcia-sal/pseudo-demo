def find_longest_repeated_substring(input_string):
    length_of_input = len(input_string)
    longest_repeat_length = 0

    # Iterate through possible substring lengths
    for substring_length in range(length_of_input):
        # Iterate through possible starting indices for the substring
        for start_index in range(length_of_input - substring_length):
            current_substring = input_string[start_index:start_index + substring_length]

            # Check if the current substring appears later in the string
            if current_substring in input_string[start_index + 1:]:
                longest_repeat_length = substring_length
                break  # Exit the inner loop if a repetition is found

    return longest_repeat_length

# Main execution
input_line = input()[:-1]  # Read input and remove the last character
print(find_longest_repeated_substring(input_line))
