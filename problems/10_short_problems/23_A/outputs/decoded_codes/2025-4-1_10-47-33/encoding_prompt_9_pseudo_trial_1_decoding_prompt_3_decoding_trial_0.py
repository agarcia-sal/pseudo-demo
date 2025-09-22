def longest_repeated_substring():
    input_string = input()[:-1]  # Read input and remove the last character.
    length_of_string = len(input_string)
    longest_repeated_length = 0

    # Iterate through substring lengths from 0 to length_of_string - 1
    for substring_length in range(1, length_of_string):
        # Check for each possible starting index for the substring of the given length
        for index in range(length_of_string - substring_length + 1):
            current_substring = input_string[index:index + substring_length]

            # Check if current_substring appears again in the input_string starting from index + 1
            if current_substring in input_string[index + 1:]:
                longest_repeated_length = substring_length

                # Exit the inner loop as we found a repeated substring of this length
                break

    print(longest_repeated_length)

# Call the function to execute
longest_repeated_substring()
