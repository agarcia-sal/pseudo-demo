def find_longest_repeating_substring():
    # Step 1: Read Input
    input_string = input()  # Read input from the user
    string_length = len(input_string)  # Store the length of the string
    longest_repeating_substring_length = 0  # Initialize the maximum length found

    # Step 2: Iterate Through Substring Lengths
    for current_length in range(1, string_length):  # Starting from length 1 to string_length-1
        for start_index in range(string_length - current_length):  # Ensure valid start indexes
            # Extract substring
            substring = input_string[start_index:start_index + current_length]

            # Search for repeats
            if substring in input_string[start_index + current_length:]:  # Check in the remaining string
                longest_repeating_substring_length = current_length  # Update the maximum length
                break  # No need to check further for this length

    # Step 3: Output Result
    print(longest_repeating_substring_length)

# Example Usage:
find_longest_repeating_substring()
