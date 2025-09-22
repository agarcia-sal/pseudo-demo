def find_longest_repeated_substring(input_string):
    length_of_input = len(input_string)
    longest_repeat_length = 0

    for substring_length in range(1, length_of_input):  # start substring length from 1
        for start_index in range(length_of_input - substring_length + 1):
            current_substring = input_string[start_index:start_index + substring_length]

            # Check if currentSubstring can be found starting from the next position
            if current_substring in input_string[start_index + 1:]:
                longest_repeat_length = substring_length
                break  # Exit the inner loop if a repeat is found

    return longest_repeat_length

# Execution of the function
line = input()[:-1]  # Read user input and remove the last character
print(find_longest_repeated_substring(line))
