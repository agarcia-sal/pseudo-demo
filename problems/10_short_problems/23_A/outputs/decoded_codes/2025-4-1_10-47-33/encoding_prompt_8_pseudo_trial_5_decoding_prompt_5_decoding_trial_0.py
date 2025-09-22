# Function to find the length of the longest repeated substring
def longest_repeated_substring_length():
    # Read the input line from the user
    input_line = input().rstrip()  # Remove trailing newline
    length_of_input = len(input_line)  # Calculate length of the input line

    longest_repeated_substring_length = 0  # Initialize the maximum length of substrings found

    # Loop through all possible lengths of substrings
    for substring_length in range(1, length_of_input):  # Starting from length 1
        # Loop through each starting position for the substring of the current length
        for start_index in range(length_of_input - substring_length + 1):
            # Extract the substring
            current_substring = input_line[start_index:start_index + substring_length]

            # Check if this substring appears again in the input string
            if input_line.find(current_substring, start_index + 1) != -1:
                # Update longest substring length if found
                longest_repeated_substring_length = substring_length
                break  # Break inner loop to avoid further checks for this size

    # Output the maximum length of the repeated substring found
    print(longest_repeated_substring_length)

# Call the function to execute
longest_repeated_substring_length()
