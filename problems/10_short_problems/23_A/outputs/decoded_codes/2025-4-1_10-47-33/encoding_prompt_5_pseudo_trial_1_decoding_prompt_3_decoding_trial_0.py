def find_longest_repeating_substring():
    # Accept input from the user
    line = input().rstrip()  # Read the line and remove trailing whitespace
    n = len(line)  # Determine the length of the input string

    maximum_length = 0  # Initialize variable to keep track of the maximum length

    # Loop through possible substring lengths from 1 to n-1
    for l in range(1, n):
        # Inner loop to check substrings of length l
        for i in range(n - l):  # Substring starting position
            substring = line[i:i + l]  # Extract the substring

            # Check if the substring exists later in the string
            if substring in line[i + 1:]:
                maximum_length = l  # Update the maximum length found
                break  # Exit the inner loop, go to the next length

    # Output the result
    print(maximum_length)

# Example usage:
find_longest_repeating_substring()
