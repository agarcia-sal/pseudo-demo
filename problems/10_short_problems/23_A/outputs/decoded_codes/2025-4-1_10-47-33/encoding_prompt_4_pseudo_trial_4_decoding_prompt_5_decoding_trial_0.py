def longest_repeated_substring_length():
    # Read a line of input
    line = input().rstrip()  # Remove any trailing newline character
    n = len(line)  # Get the length of the input line
    longest_repeated_length = 0  # Initialize longest repeated length

    # Iterate through possible lengths of substrings
    for length in range(n):
        # Check for repeated substrings of the current length
        for start_index in range(n - length):
            # Extract the substring
            substring = line[start_index:start_index + length + 1]  # Adjusting length for slicing

            # Check if the substring occurs again after the current index
            if substring in line[start_index + 1:]:  # Check in the remainder of the string
                longest_repeated_length = length + 1  # Update length
                break  # Exit the inner loop if a repeat is found

    # Output the length of the longest repeated substring
    print(longest_repeated_length)

# Test cases could include:
# Input: "banana"
# Expected Output: 3
# Input: "abcdef"
# Expected Output: 0
