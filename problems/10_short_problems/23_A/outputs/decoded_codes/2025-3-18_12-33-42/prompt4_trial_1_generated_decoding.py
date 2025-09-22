def find_longest_repeating_substring(input_string):
    # Initialize the length of the input string
    n = len(input_string)
    # Initialize a variable to store the length of the longest repeating substring
    longest_repeating_length = 0

    # Loop through all possible lengths of substrings
    for length in range(1, n):  # Start from length 1 up to n-1
        # Check each starting position in the string
        for start_index in range(n - length):  # Ensure we don't exceed string bounds
            # Extract the substring of the current length starting from start_index
            substring = input_string[start_index:start_index + length]
            
            # Check if the substring appears again in the remainder of the string
            if substring in input_string[start_index + 1:]:
                # Update the longest repeating length
                longest_repeating_length = length
                # Exit the inner loop as we found a repeating substring
                break  # Found a substring of current length that repeats, break inner loop

    # Output the length of the longest repeating substring found
    return longest_repeating_length


# Test cases
print(find_longest_repeating_substring("abcabc"))  # Expected output: 3 (substring "abc" repeats)
print(find_longest_repeating_substring("aabbcc"))  # Expected output: 2 (substrings "a", "b", and "c" repeat)
print(find_longest_repeating_substring("hello"))    # Expected output: 1 (substring "l" repeats)
print(find_longest_repeating_substring("abcdef"))   # Expected output: 0 (no repeats)
print(find_longest_repeating_substring(""))          # Expected output: 0 (empty string)
