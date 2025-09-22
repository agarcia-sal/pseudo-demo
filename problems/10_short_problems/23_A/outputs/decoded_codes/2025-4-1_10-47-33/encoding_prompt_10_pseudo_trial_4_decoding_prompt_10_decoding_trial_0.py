def find_longest_repeated_substring():
    # Read a line of input from the user and remove the newline character
    line = input().strip()

    # Determine the length of the input line
    n = len(line)
    longest_repeated_length = 0  # Initialize the result variable

    # Loop through all possible lengths of substrings from 0 to n-1
    for l in range(n):
        # Loop through the starting index of the substring
        for i in range(n):
            # Extract the substring from index i with length l
            substring = line[i:i+l]
            # Check if the substring exists later in the string
            if substring and line.find(substring, i + 1) != -1:
                longest_repeated_length = l  # Update result variable with current length l
                break  # Exit the inner loop if a repeated substring is found

    # Print the result variable indicating the length of the substring found
    print(longest_repeated_length)

# Call the function to execute
find_longest_repeated_substring()
