def longest_repeated_substring():
    # Read input string from standard input
    input_string = input().strip()[:-1]  # Strip any trailing newline and remove the last character
    length_of_string = len(input_string)
    longest_repeated_length = 0

    # Iterate over possible substring lengths from 1 to length_of_string
    for substring_length in range(1, length_of_string):
        for index in range(length_of_string - substring_length + 1):
            current_substring = input_string[index:index + substring_length]

            # Check if current_substring appears again in input_string from the next index
            if current_substring in input_string[index + substring_length:]:
                longest_repeated_length = substring_length
                break  # Exit inner loop if we found a repeated substring

    print(longest_repeated_length)  # Output the length of the longest repeated substring

# Call the function to execute
longest_repeated_substring()
