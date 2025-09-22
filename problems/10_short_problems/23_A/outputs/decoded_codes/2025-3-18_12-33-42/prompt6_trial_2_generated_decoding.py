def main():
    # Read input string from the user
    input_string = input().strip()  # Remove any extra whitespace, especially newlines
    length_of_input = len(input_string)
    longest_repeated_substring_length = 0

    # Loop through possible lengths of substrings
    for substring_length in range(1, length_of_input):
        # Check each starting position for the substring
        for starting_index in range(length_of_input):
            # Extract the substring starting from the current index with the current length
            current_substring = extract_substring(input_string, starting_index, substring_length)

            # Check if the current substring appears again in the rest of the string
            if substring_exists_in_rest_of_string(input_string, current_substring, starting_index):
                longest_repeated_substring_length = substring_length  # Update longest length found
                break  # Exit the inner loop if a repeat is found

    # Output the length of the longest repeated substring found
    print(longest_repeated_substring_length)

def extract_substring(input_string, starting_index, substring_length):
    # Return the substring of the input string starting at starting_index with the specified length
    return input_string[starting_index:starting_index + substring_length]

def substring_exists_in_rest_of_string(input_string, current_substring, starting_index):
    # Check if current_substring occurs in input_string after the starting_index
    return current_substring in input_string[starting_index + 1:]

# Invoke the main function to run the program
main()
