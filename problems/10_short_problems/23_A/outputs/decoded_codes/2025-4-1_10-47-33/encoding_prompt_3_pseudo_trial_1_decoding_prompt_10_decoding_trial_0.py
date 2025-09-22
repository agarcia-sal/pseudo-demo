def longest_repeated_substring_length():
    # Read a line of input and remove the last character
    string_line = input().strip()[:-1]  # Remove the last character
    length_of_string = len(string_line)
    longest_repeated_substring_length = 0

    # Iterate over possible lengths of substrings
    for substring_length in range(1, length_of_string + 1):  # Substring lengths from 1 to length_of_string
        found_repeated = False  # Flag to note if a repeated substring is found

        # Check for each starting position of the string
        for starting_index in range(length_of_string - substring_length + 1):
            # Create a substring of the current length starting from starting_index
            current_substring = string_line[starting_index:starting_index + substring_length]
            
            # Check if the current substring appears again in the string
            if current_substring in string_line[starting_index + 1:]:
                # Update the longest repeated substring length found
                longest_repeated_substring_length = substring_length
                found_repeated = True
                break  # Exit inner loop if a repetition is found

        if found_repeated:
            continue  # Go to the next substring length iteration

    # Output the longest length of the repeated substring found
    print(longest_repeated_substring_length)

# Testing the function with various cases
longest_repeated_substring_length()
