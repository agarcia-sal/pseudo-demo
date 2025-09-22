def find_longest_repeated_substring(input_string):
    length_of_string = len(input_string)
    longest_repeated_substring_length = 0

    # Check for all possible substring lengths
    for substring_length in range(1, length_of_string):  # substring lengths from 1 to length_of_string - 1
        for start_index in range(length_of_string - substring_length + 1):  # valid starting indices
            current_substring = input_string[start_index:start_index + substring_length]
            # Check if current substring appears again after its starting index
            if current_substring in input_string[start_index + 1:]:
                longest_repeated_substring_length = substring_length
                break  # Found a repeat, break out of inner loop

    return longest_repeated_substring_length

# Driver code
input_string = input()  # Read input from standard input
print(find_longest_repeated_substring(input_string))
