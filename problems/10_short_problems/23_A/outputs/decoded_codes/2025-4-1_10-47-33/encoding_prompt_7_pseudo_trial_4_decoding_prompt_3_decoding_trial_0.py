def find_longest_repeated_substring(input_string):
    length_of_string = len(input_string)
    longest_repeated_substring_length = 0

    # Iterate over possible substring lengths
    for substring_length in range(1, length_of_string):  # Start from 1 since length 0 is not meaningful
        for start_index in range(length_of_string - substring_length + 1):
            # Extract the current substring
            current_substring = input_string[start_index:start_index + substring_length]
            # Check if this substring appears again after the current start_index
            if current_substring in input_string[start_index + 1:]:
                longest_repeated_substring_length = substring_length
                break  # Exit the inner loop when a repeat is found
    
    return longest_repeated_substring_length


# Driver code
input_string = input().strip()  # Read input and remove trailing newline characters
print(find_longest_repeated_substring(input_string))
