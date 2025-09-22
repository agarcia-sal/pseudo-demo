def find_longest_repeated_substring(input_string):
    # Get the length of the input string
    string_length = len(input_string)
    longest_repetition_length = 0

    # Iterate over possible lengths for substrings from 1 to string_length
    for length in range(1, string_length):
        # Create a set to store seen substrings
        seen_substrings = set()
        
        # Check each substring of the current length
        for start in range(string_length - length + 1):
            substring = input_string[start:start + length]
            
            # If the substring has been seen before, update longest repetition length
            if substring in seen_substrings:
                longest_repetition_length = length
            else:
                seen_substrings.add(substring)

    # Return the length of the longest repeated substring found
    return longest_repetition_length

# Example test cases
if __name__ == "__main__":
    test_string = input()
    result = find_longest_repeated_substring(test_string)
    print(result)
