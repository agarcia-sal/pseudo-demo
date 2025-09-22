def find_longest_repeated_substring(input_string):
    """
    Finds the length of the longest repeated substring in the given input string.
    
    Args:
        input_string (str): The input string in which to find repeated substrings.

    Returns:
        int: The length of the longest repeated substring.
    """
    trimmed_string = remove_trailing_newline(input_string)
    string_length = len(trimmed_string)
    longest_repeated_length = 0

    # Loop through possible substring lengths
    for length_index in range(1, string_length):  # Start from 1 to avoid zero-length substrings
        for start_index in range(string_length - length_index + 1):  # Ensure valid substring extraction
            current_substring = trimmed_string[start_index:start_index + length_index]
            if find(trimmed_string, current_substring, start_index + 1):
                longest_repeated_length = length_index
                break  # Exit inner loop if a repeated substring is found
        else:
            continue  # Only executed if the inner loop did NOT break
        break  # Inner loop found a duplicate, break the outer loop

    return longest_repeated_length

def remove_trailing_newline(string):
    """
    Removes the trailing newline character from the input string.
    
    Args:
        string (str): The input string to process.

    Returns:
        str: The input string without the trailing newline character.
    """
    return string.rstrip('\n')

def find(source_string, sub_string, start_index=0):
    """
    Finds the index of sub_string in source_string starting from start_index.
    
    Args:
        source_string (str): The string to be searched.
        sub_string (str): The substring to find.
        start_index (int): The index to start the search from.

    Returns:
        int: The index of sub_string in source_string, or -1 if not found.
    """
    index = source_string.find(sub_string, start_index)
    return index if index != -1 else -1

# Example usage:
# input_string = input()
# print(find_longest_repeated_substring(input_string))
