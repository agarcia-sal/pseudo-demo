def find_longest_repeated_substring():
    # Read input string from the user
    input_string = input()
    # Get the length of the input string
    string_length = len(input_string)
    # Initialize variable to hold the length of the longest repetition found
    longest_repetition_length = 0

    # Loop through possible substring lengths from 0 to string_length - 1
    for length in range(1, string_length):  # starting from 1 because a length of 0 will not yield substrings
        # Loop through the starting position of the substring
        for start_position in range(string_length - length):
            # Extract the substring of the current length
            substring = input_string[start_position:start_position + length]
            # Check if this substring occurs again in the string starting from start_position + 1
            if substring in input_string[start_position + length:]:
                longest_repetition_length = length
                break  # Break out of the inner loop if a repetition is found

    # Output the length of the longest repeated substring found
    print(longest_repetition_length)

# Call the function to execute
find_longest_repeated_substring()
