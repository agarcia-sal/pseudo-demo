def find_longest_repeated_substring():
    # Accept string input from the user
    input_string = input()
    
    # Determine the length of the string
    string_length = len(input_string)
    longest_repeated_length = 0  # This will store the length of the longest repeated substring

    # Outer loop: iterate over possible lengths of substrings
    for possible_length in range(1, string_length):  # starting from 1 for non-empty substrings
        # Inner loop: iterate over each starting position for the substring of the current possible length
        for starting_index in range(string_length - possible_length):
            # Extract the substring starting at starting_index with the current possible_length
            substring = input_string[starting_index:starting_index + possible_length]

            # Check if this substring exists again in the remaining part of the string
            if substring_exists_in_rest_of_string(input_string, substring, starting_index):
                longest_repeated_length = possible_length  # Update longest length found
                break  # No need to check further for this length

    # Output the length of the longest repeated substring
    print(longest_repeated_length)


def substring_exists_in_rest_of_string(input_string, substring, starting_index):
    # Check for the substring in the part of the string after the starting index
    position_found = input_string.find(substring, starting_index + 1)

    # Return true if a position was found, otherwise false
    return position_found != -1


# Example test cases (uncomment to run tests)
# Input: "abcabc"
# Expected output: 3 (substring "abc" appears twice)
# find_longest_repeated_substring()

# Input: "abcdefgh"
# Expected output: 0 (no substring repeats)
# find_longest_repeated_substring()
