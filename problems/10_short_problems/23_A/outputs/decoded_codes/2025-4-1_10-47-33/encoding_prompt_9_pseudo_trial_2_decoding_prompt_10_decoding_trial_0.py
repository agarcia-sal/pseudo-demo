def longest_repeating_substring():
    # Read input string
    input_string = input()  
    # Store the length of the string
    string_length = len(input_string)
    # Initialize the longest repeating substring length to zero
    longest_repeating_length = 0

    # Iterate through substring lengths from 1 to string_length - 1
    for current_length in range(1, string_length):
        # Check all starting positions for the substrings of length current_length
        for start_index in range(string_length - current_length):
            # Extract the substring
            substring = input_string[start_index:start_index + current_length]

            # Search for the substring in the remaining part of the string
            if substring in input_string[start_index + 1:]:
                # Update the longest repeating substring length
                longest_repeating_length = current_length
                # Exit inner loop when a repeating substring is found
                break

    # Output the result
    print(longest_repeating_length)

# Call the function to execute
longest_repeating_substring()
