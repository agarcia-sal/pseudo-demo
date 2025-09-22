def longest_repeated_substring_length():
    # Read a line of input from standard input
    string_input = input().strip()  # Remove the newline character

    # Determine the length of the input string
    string_length = len(string_input)

    # Initialize variable to hold the result
    longest_repeated_substring_length = 0

    # Loop through lengths of potential substrings from 1 to string_length
    for length_from_one in range(1, string_length):
        # Loop through each starting index for the substrings
        for start_index in range(string_length - length_from_one + 1):
            # Extract the substring of the current length
            current_substring = string_input[start_index:start_index + length_from_one]

            # Check if the current substring can be found in the remainder of the string
            if current_substring in string_input[start_index + 1:]:
                # If found, update the result to the current length
                longest_repeated_substring_length = length_from_one
                break  # Exit the loop since we found a repeated substring of this length

        # If we found a repeated substring of this length, no need to check longer lengths
        if longest_repeated_substring_length == length_from_one:
            continue

    # Output the length of the longest repeated substring found
    print(longest_repeated_substring_length)

# Example test case (uncomment to test)
# Expected output for input "banana" is 3 ("ana" is the longest repeated substring)
# longest_repeated_substring_length()
