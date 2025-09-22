def longest_repeated_substring():
    # Read an input string from standard input
    input_string = input().strip()  # Using strip to remove potential trailing newline or spaces
    length_of_string = len(input_string)
    repeated_substring_length = 0

    # Iterate over possible lengths for substrings
    for length in range(1, length_of_string):  # start from 1 to avoid empty substring
        found_repetition = False

        # Iterate through the starting index of the substring
        for index in range(length_of_string - length + 1):
            substring = input_string[index:index + length]

            # Check if the substring is found later in the string
            if substring in input_string[index + 1:]:
                repeated_substring_length = length
                found_repetition = True
                break  # Break out of the inner loop if a repetition is found

        if found_repetition:
            continue  # Continue the outer loop to check for longer substrings

    # Output the length of the longest repeated substring found
    print(repeated_substring_length)

# Call the function to execute
longest_repeated_substring()
