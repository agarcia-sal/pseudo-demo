def find_longest_repeated_substring(input_string):
    length_of_input = len(input_string)
    longest_repeat_length = 0

    for substring_length in range(1, length_of_input):  # Start from 1 to avoid empty substring
        for start_index in range(length_of_input - substring_length + 1): 
            current_substring = input_string[start_index:start_index + substring_length]

            # Check if the current substring exists later in the string
            if current_substring in input_string[start_index + 1:]:
                longest_repeat_length = substring_length
                break  # Found a repeating substring, break out of inner loop

    return longest_repeat_length


# Main execution
line = input()[:-1]  # Get input and remove the last character
print(find_longest_repeated_substring(line))
