def longest_repeating_substring():
    # Read a line of input from the user
    line = input()
    
    # Get the length of the input line
    n = len(line)

    # Initialize return value
    longest_repeating_length = 0

    # Iterate over possible substring lengths from 1 to n (inclusive)
    for length in range(1, n + 1):
        # Check for each starting index in the string
        for start_index in range(n - length + 1):
            # Extract the substring of the current length
            substring = line[start_index:start_index + length]

            # Check if this substring exists again in the string after the start_index
            if substring in line[start_index + length:]:
                # Update longest repeating length if found
                longest_repeating_length = length

    # Output the length of the longest repeating substring found
    print(longest_repeating_length)

# Call the function to execute
longest_repeating_substring()
