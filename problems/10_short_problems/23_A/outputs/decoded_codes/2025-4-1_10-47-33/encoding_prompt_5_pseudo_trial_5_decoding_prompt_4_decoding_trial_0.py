def find_longest_repeated_substring():
    # Read input from the user
    input_string = input().rstrip()  # Remove the newline character
    
    # Get the length of the input string
    length_of_string = len(input_string)
    longest_repeated_length = 0

    # Loop through possible substring lengths
    for length in range(1, length_of_string):  # Start from 1 to avoid empty substring
        # Nested loop to check every position in the string
        for position in range(length_of_string - length + 1):  # Avoid out-of-bounds
            # Extract the substring of the current length starting from the current position
            current_substring = input_string[position:position + length]

            # Check if this substring appears again in the string
            if current_substring in input_string[position + 1:]:
                # Update the longest length if a repeated substring is found
                longest_repeated_length = length
                break  # No need to check further for this length

    # Output the length of the longest repeated substring found
    print(longest_repeated_length)

# Function call to execute the code
find_longest_repeated_substring()
