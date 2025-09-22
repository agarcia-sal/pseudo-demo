def longest_repeated_substring_length():
    # Receive Input
    input_string = input().rstrip('\n')  # Read and strip newline character
    length_of_string = len(input_string)
    longest_repeated_substring_length = 0

    # Loop Through Substring Lengths
    for current_length in range(length_of_string):
        for start_index in range(length_of_string - current_length):
            substring = input_string[start_index:start_index + current_length + 1]  # Extract the substring
            # Check if this substring occurs again in the string
            if substring in input_string[start_index + 1:]:
                longest_repeated_substring_length = current_length + 1  # Update if found
                break  # Break out of the inner loop as we found a repeated substring
            
    # Output Result
    print(longest_repeated_substring_length)

# Calling the function to execute the logic
longest_repeated_substring_length()
