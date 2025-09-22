def find_longest_repeated_substring(input_string):
    # Get the length of the input string
    string_length = len(input_string)
    longest_repetition_length = 0

    # Iterate over possible lengths for substrings from 0 to string_length - 1
    for l in range(string_length):
        # Iterate over each possible starting index of the substring
        for i in range(string_length):
            # Define the substring from the current position and length
            substring = input_string[i:i+l+1]
            # Check if this substring exists later in the input string
            if input_string.find(substring, i + 1) != -1:
                # If found, update longest repetition length
                longest_repetition_length = l + 1
                break  # Exit inner loop if a repetition is found

    # Return the length of the longest repeated substring found
    return longest_repetition_length
