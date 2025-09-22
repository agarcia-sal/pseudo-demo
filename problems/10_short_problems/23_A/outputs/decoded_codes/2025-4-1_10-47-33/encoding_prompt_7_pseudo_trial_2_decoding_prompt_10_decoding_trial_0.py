def find_longest_repeated_substring(input_string):
    # Get the length of the input string
    string_length = len(input_string)
    longest_repetition_length = 0

    # Iterate over possible lengths for substrings from 0 to string_length - 1
    for l in range(1, string_length):  # Starting from 1 to avoid empty substring
        # Use a set to track visited substrings of length l
        seen_substrings = set()
        # Iterate over each possible starting index of the substring
        for i in range(string_length - l + 1):
            # Extract the substring of length l starting at index i
            substring = input_string[i:i + l]
            # Check if the substring has been seen before
            if substring in seen_substrings:
                # If found, update longest repetition length and break the loop
                longest_repetition_length = l
                break
            # Add the substring to the set of seen substrings
            seen_substrings.add(substring)
        if longest_repetition_length == l:  # Break outer loop as well
            break

    # Return the length of the longest repeated substring found
    return longest_repetition_length


# Test cases
print(find_longest_repeated_substring("banana"))  # Expected output: 2 ("an" or "na")
print(find_longest_repeated_substring("abcde"))    # Expected output: 0 (no repeats)
print(find_longest_repeated_substring("aabbcc"))    # Expected output: 2 ("a" or "b" or "c")
print(find_longest_repeated_substring("abcdefabcdef"))  # Expected output: 6 ("abcdef")
print(find_longest_repeated_substring(""))  # Expected output: 0 (empty string)
