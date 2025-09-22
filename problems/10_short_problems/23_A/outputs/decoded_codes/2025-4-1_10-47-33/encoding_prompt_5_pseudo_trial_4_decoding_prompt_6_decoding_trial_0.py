# Function to find the length of the longest repeating substring
def find_longest_repeated_substring_length():
    # Read input and remove newline character
    input_string = input().strip()
    length_of_input = len(input_string)  # Length of the input string
    longest_repeated_substring_length = 0  # Initialize to zero

    # Check for substrings of increasing length
    for current_length in range(length_of_input):  # Iterate from 0 to length_of_input - 1
        # Iterate through the starting index of the substring
        for start_index in range(length_of_input):  # Iterate from 0 to length_of_input - 1
            # Create a substring of length (current_length + 1)
            substring = input_string[start_index:start_index + current_length + 1]
            # Check if this substring appears again in the input
            if input_string.find(substring, start_index + 1) != -1:  # Check after current start_index
                # Update the longest repeating substring length
                longest_repeated_substring_length = current_length + 1
                break  # Exit the inner loop since we found a repeat

    # Output the length of the longest repeating substring
    print(longest_repeated_substring_length)

# Call the function to execute
find_longest_repeated_substring_length()
