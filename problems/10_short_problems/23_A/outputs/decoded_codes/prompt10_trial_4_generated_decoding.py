def longest_repeated_substring():
    # Read a line of input and remove the trailing newline character
    line = input().strip()
    n = len(line)
    longest_length = 0  # Variable to store the length of the longest repeated substring
    
    # Loop through each possible length of substring
    for length in range(1, n):  # substring lengths from 1 to n-1
        # Loop through each starting index of the substring
        for start_index in range(n - length + 1):  # valid starting indices for this length
            # Extract a substring of the current length starting from start_index
            substring = line[start_index:start_index + length]
            # Check if this substring appears again in the line after start_index
            if substring in line[start_index + length:]:
                longest_length = length  # Update longest_length with the current length
                break  # Exit the inner loop once we find a repetition
        if longest_length:  # If we've found at least one repeated length, we can stop looking for longer lengths
            break

    # Output the result
    print(longest_length)

# Test the function with various inputs
if __name__ == "__main__":
    # You can replace these tests with actual input during execution
    import io
    import sys
    
    # Redirect standard input to simulate input() for testing purpose
    test_inputs = [
        "banana\n",
        "abcde\n",
        "aabbcc\n",
        "xyzxyz\n",
        "abcdabc\n"
    ]

    for test_input in test_inputs:
        sys.stdin = io.StringIO(test_input)  # Simulate input
        longest_repeated_substring()
