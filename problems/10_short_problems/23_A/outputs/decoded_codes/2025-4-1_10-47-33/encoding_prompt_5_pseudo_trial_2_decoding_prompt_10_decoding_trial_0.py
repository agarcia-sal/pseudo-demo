def find_length_of_longest_repeating_substring():
    # Accept input from user
    input_string = read_input_string()  # Read a line of input from the user
    string_length = len(input_string)  # Calculate the length of the input string
    longest_repeating_length = 0  # Initialize the length of the longest repeating substring

    # Iterate over all possible lengths of substrings
    for substring_length in range(1, string_length):  # Start from 1 for a valid substring
        # Check for each starting position in the string
        for start_index in range(string_length - substring_length + 1):
            # Extract the substring from the current index of specified length
            current_substring = extract_substring(input_string, start_index, substring_length)

            # Check if this current substring exists later in the input_string
            if exists_in_string(input_string, current_substring, start_index + 1):
                # Update longest_repeating_length
                longest_repeating_length = substring_length
                break  # Stop checking this length since we've found a match

    # Output the length of the longest repeating substring found
    print(longest_repeating_length)


def read_input_string():
    return input()  # Read a line of input from the user


def extract_substring(input_string, start_index, length):
    return input_string[start_index:start_index + length]  # Extract substring


def exists_in_string(input_string, substring, start_index):
    # Check if substring appears in input_string starting from start_index
    return substring in input_string[start_index:]  # Check for existence from the start_index


# Test the function
if __name__ == "__main__":
    find_length_of_longest_repeating_substring()
