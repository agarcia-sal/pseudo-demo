def find_longest_repeating_substring():
    # Accept input from the user and strip trailing newline or whitespace
    input_string = input().strip()
    n = len(input_string)  # Determine the length of the input string
    maximum_length = 0  # Initialize the maximum length of the repeating substring

    # Loop through possible substring lengths
    for length in range(1, n):  # Start from 1 since a substring length of 0 is not meaningful
        for start in range(n - length):  # Iterate through valid starting positions
            substring = input_string[start:start + length]  # Extract the current substring
            # Check if the substring can be found again in the rest of the string
            if substring in input_string[start + 1:]:  # Search from the next position
                maximum_length = length  # Update the maximum length found
                break  # Exit inner loop, as we found a repeating substring

    print(maximum_length)  # Output the maximum length of the repeating substring

# Call the function to execute
find_longest_repeating_substring()
