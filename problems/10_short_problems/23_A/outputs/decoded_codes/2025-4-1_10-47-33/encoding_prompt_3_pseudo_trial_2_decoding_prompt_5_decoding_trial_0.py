# This function finds the length of the longest repeated substring in a given input string.
def longest_repeated_substring_length():
    # Read a line of input
    line = input().strip()
    n = len(line)
    repeated_length = 0  # This will hold the length of the longest repeated substring

    # Outer loop: Check all possible substring lengths from 0 to n-1
    for possible_length in range(n):
        # Inner loop: Check all starting positions for substrings of current possible_length
        for index in range(n):
            # Extract substring of current possible_length
            substring = line[index:index + possible_length]

            # Check if the substring appears later in the string
            if substring in line[index + 1:]:  # Only check after the current index
                repeated_length = possible_length  # Update repeated_length
                break  # Exit inner loop as we found a repeated substring

    # Output the length of the longest repeated substring found
    print(repeated_length)

# Example test cases (uncomment to run):
# Input: "abcabc"
# Output: 3 (the substring "abc" is repeated)
# longest_repeated_substring_length()
