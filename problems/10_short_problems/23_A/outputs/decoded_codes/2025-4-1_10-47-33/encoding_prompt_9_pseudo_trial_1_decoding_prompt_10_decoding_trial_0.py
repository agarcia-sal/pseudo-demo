def find_longest_repeated_substring():
    # Read input from the user, excluding the last character (to follow the pseudocode)
    input_string = input()[:-1]  
    length_of_string = len(input_string)
    longest_repeated_length = 0

    # Iterate over possible substring lengths from 1 to length_of_string
    for substring_length in range(1, length_of_string):
        # Check each starting index for substrings of the current length
        for index in range(length_of_string - substring_length + 1):
            # Generate the current substring
            current_substring = input_string[index:index + substring_length]

            # Check if current_substring appears again in input_string starting from index + 1
            if current_substring in input_string[index + 1:]:
                longest_repeated_length = substring_length
                # Break out of the inner loop as we found a repeating substring
                break

    # Output the length of the longest repeated substring found
    print(longest_repeated_length)

# Call the function to execute
find_longest_repeated_substring()
