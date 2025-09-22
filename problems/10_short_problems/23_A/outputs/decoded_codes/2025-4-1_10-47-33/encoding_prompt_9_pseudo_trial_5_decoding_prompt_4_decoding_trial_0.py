def longest_repeated_substring():
    # Step 1: Get the input
    input_string = input().strip()  # Read and strip trailing newline characters
    string_length = len(input_string)
    longest_repeated_substring_length = 0  # Initialize the result

    # Step 2: Iterate over possible substring lengths
    for current_length in range(1, string_length):  # Starting from 1 to string_length - 1
        for start_position in range(string_length - current_length):
            # Extract the substring
            substring = input_string[start_position:start_position + current_length]
            # Check if this substring appears again in the remainder of the string
            if substring in input_string[start_position + current_length:]:
                longest_repeated_substring_length = current_length  # Update max length found
                break  # Exit the inner loop since we found a repeated substring

    # Step 3: Output the length
    print(longest_repeated_substring_length)

# Call the function to execute
longest_repeated_substring()
