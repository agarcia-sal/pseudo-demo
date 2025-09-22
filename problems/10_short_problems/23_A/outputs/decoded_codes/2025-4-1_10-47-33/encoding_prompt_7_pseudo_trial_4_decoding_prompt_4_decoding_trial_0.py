def find_longest_repeated_substring(input_string):
    length_of_string = len(input_string)
    longest_repeated_substring_length = 0

    # Check all possible substring lengths
    for substring_length in range(1, length_of_string):  # start from 1 to avoid empty substring
        # Check each starting index for this substring length
        for start_index in range(length_of_string - substring_length + 1):
            current_substring = input_string[start_index:start_index + substring_length]

            # Check if the current substring appears again
            if input_string.find(current_substring, start_index + 1) != -1:
                longest_repeated_substring_length = substring_length
                break  # Break the inner loop as we found a repeated substring

    return longest_repeated_substring_length


# Driver code
input_string = input().strip()  # Read input from standard input
print(find_longest_repeated_substring(input_string))
