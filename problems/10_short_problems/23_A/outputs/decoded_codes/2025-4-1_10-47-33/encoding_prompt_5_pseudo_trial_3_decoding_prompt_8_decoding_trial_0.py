def longest_repeated_substring():
    # Read a line of input from the user
    line = input()

    # Remove the newline character from the end of the input
    line = line.rstrip('\n')

    # Calculate the length of the input string
    n = len(line)

    # Initialize a variable to hold the length of the longest repeated substring
    longest_repeated_length = 0

    # Loop through substrings of increasing lengths
    for length in range(n):
        # Check all starting positions for the substring of the current length
        for start_position in range(n):
            if start_position + length <= n:
                # Extract the substring from 'start_position' of 'length'
                current_substring = line[start_position:start_position + length]

                # Check if this substring appears again in the string after its starting position
                if current_substring in line[start_position + 1:]:
                    # If the substring is found again, update the longest repeated length
                    longest_repeated_length = length + 1  # length is zero-indexed
                    break  # Exit this inner loop as we found a repeat

    # Print the length of the longest repeated substring found
    print(longest_repeated_length)

# Call the function to run the program
longest_repeated_substring()
