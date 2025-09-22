def longest_repeated_substring():
    input_string = input().rstrip('\n')
    length_of_string = len(input_string)
    longest_repeated_substring_length = 0

    for current_length in range(1, length_of_string):  # Start from length 1
        for start_index in range(length_of_string - current_length):
            substring = input_string[start_index:start_index + current_length]
            if substring in input_string[start_index + current_length:]:
                longest_repeated_substring_length = current_length
                break  # Found a repeated substring, break to look for a longer one

    print(longest_repeated_substring_length)

# Uncomment to test the function
# longest_repeated_substring()
