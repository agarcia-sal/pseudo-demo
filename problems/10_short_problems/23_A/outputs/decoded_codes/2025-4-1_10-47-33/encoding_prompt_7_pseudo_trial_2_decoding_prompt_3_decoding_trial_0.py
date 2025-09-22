def find_longest_repeated_substring(input_string):
    # Get the length of the input string
    string_length = len(input_string)
    longest_repetition_length = 0

    # Check substrings of length ranging from 1 to string_length - 1
    for length in range(1, string_length):  # lengths start from 1
        # Iterate over the starting index of the substring
        for start in range(string_length - length):
            # Define the substring of the current length
            substring = input_string[start:start + length]
            # Check if the substring exists later in the string
            if substring in input_string[start + length:]:
                longest_repetition_length = length
                break  # Exit inner loop if a repetition is found
        else:
            continue  # Only executed if inner loop did NOT break
        break  # Exit outer loop if we found at least one repetition

    # Return the length of the longest repeated substring found
    return longest_repetition_length

# Example usage
# Uncomment the following lines to test the function
# input_string = input()
# print(find_longest_repeated_substring(input_string))
