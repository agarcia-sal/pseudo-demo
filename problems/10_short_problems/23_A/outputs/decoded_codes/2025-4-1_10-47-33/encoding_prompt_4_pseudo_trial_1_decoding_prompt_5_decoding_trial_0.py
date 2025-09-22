def find_longest_repeating_substring_length():
    # Read a line of input from the user
    line = input()
    
    # Get the length of the input line
    n = len(line)

    # Initialize return value for the longest repeating length
    longest_repeating_length = 0

    # Iterate over possible substring lengths
    for length in range(1, n):  # lengths should start from 1 to n-1
        # Check for each starting index in the string
        for start_index in range(n - length):  # ensure we don't go out of bounds
            # Extract the substring of the current length
            substring = line[start_index:start_index + length]

            # Check if this substring exists again in the string after the start_index
            if substring in line[start_index + length:]:
                # Update longest repeating length if found
                longest_repeating_length = length
                break  # Exit inner loop if a repeat is found

    # Output the length of the longest repeating substring found
    print(longest_repeating_length)

# Example usage:
# To test the function, you would call find_longest_repeating_substring_length() 
# and enter a string when prompted.
