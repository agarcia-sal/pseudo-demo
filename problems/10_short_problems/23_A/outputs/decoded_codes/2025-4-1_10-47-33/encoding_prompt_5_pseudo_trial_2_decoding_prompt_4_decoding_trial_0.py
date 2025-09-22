def find_length_of_longest_repeating_substring():
    # Accept input from user
    input_string = read_input_string()  
    string_length = len(input_string)  # Calculate the length of the input string
    longest_repeating_length = 0  # Initialize variable to store length of longest repeating substring

    # Iterate over all possible lengths of substrings
    for substring_length in range(1, string_length):  # Starting from 1 to avoid empty substrings
        # Check for each starting position in the string
        for start_index in range(string_length - substring_length + 1):  # Adjust the range
            # Extract the substring from current index of specified length
            current_substring = extract_substring(input_string, start_index, substring_length)

            # Check if this current substring exists later in the input_string
            if exists_in_string(input_string, current_substring, start_index + 1):
                # If it does exist, update longest_repeating_length
                longest_repeating_length = substring_length
                break  # Stop checking this length since we found a match

    # Output the length of the longest repeating substring found
    print(longest_repeating_length)


def read_input_string():
    return input()  # Read a line of input from the user


def extract_substring(string, start_index, length):
    return string[start_index:start_index + length]  # Extract substring


def exists_in_string(string, substring, start_index):
    # Check if substring appears in string starting from start_index
    return substring in string[start_index:]  # Slicing from start_index to the end for the check


# Run the function when the script is executed
if __name__ == "__main__":
    find_length_of_longest_repeating_substring()
