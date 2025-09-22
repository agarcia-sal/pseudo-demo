def find_longest_repeated_substring_length():
    # Receive Input
    input_string = input().rstrip()  # Remove any trailing newlines or spaces
    length_of_string = len(input_string)
    longest_repeated_substring_length = 0
    
    # Loop Through Substring Lengths
    for current_length in range(1, length_of_string):  # Start from 1 up to the max length - 1
        found = False  # Flag to check if we found any repeated substring of current_length
        
        for start_index in range(length_of_string - current_length + 1):
            substring = input_string[start_index:start_index + current_length]  # Extract the substring
            # Check if this substring occurs again in the string
            if substring in input_string[start_index + 1:]:
                longest_repeated_substring_length = current_length  # Update longest length
                found = True  # Mark that we found a repetition
                break  # No need to continue searching for this length
        
        if not found:
            break  # If we didn't find any substrings of current_length, stop checking longer lengths
    
    # Output Result
    print(longest_repeated_substring_length)

# Call the function to execute
find_longest_repeated_substring_length()
