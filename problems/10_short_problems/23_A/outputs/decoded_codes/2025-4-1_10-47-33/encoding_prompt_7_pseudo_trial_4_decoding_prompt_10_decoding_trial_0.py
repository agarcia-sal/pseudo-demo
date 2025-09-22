def find_longest_repeated_substring(input_string):
    """
    Function to find the length of the longest repeated substring
    in the input string.
    
    Args:
        input_string (str): The string to be analyzed.
        
    Returns:
        int: Length of the longest repeated substring.
    """
    length_of_string = len(input_string)
    longest_repeated_substring_length = 0

    # Check all possible substring lengths
    for substring_length in range(1, length_of_string):
        # Check all starting indices for substrings of this length
        for start_index in range(length_of_string - substring_length + 1):
            current_substring = input_string[start_index:start_index + substring_length]
            # Check for the occurrence of current substring again
            if input_string.find(current_substring, start_index + substring_length) != -1:
                longest_repeated_substring_length = substring_length
                break  # Found a repetition, no need to check further for this length
        else:
            continue  # Continue outer loop if not broken
        break  # Break outer loop if inner loop was broken

    return longest_repeated_substring_length


# Driver code to read input and output result
input_string = input().strip()  # Read input and remove any trailing newline
print(find_longest_repeated_substring(input_string))
