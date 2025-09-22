def longest_repeated_substring():
    # Read input from the user
    input_string = input().rstrip('\n')  # Remove the last newline character

    # Get the length of the input string
    length_of_string = len(input_string)
    longest_repeated_length = 0  # Initialize the length of the longest repeated substring

    # Loop through possible substring lengths
    for length in range(1, length_of_string):  # Starting from 1 for non-empty substrings
        # Nested loop to check every position in the string
        for position in range(length_of_string - length + 1):  # Ensure we don't go out of bounds
            # Extract the substring of current length starting from the current position
            current_substring = input_string[position:position + length]
            
            # Check if this substring appears again in the string,
            # starting just after its current position
            if current_substring in input_string[position + 1:]:
                # Update the longest length if a repeated substring is found
                longest_repeated_length = length
                # Break out of the inner loop to check longer lengths
                break

    # Output the length of the longest repeated substring found
    print(longest_repeated_length)

# Run the function
longest_repeated_substring()
