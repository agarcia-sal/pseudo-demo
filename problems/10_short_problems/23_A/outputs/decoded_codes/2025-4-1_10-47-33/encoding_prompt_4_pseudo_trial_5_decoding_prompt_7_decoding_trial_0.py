# Function to find the length of the longest repeated substring
def longest_repeated_substring():
    # Read a line of input and remove any trailing newline characters
    line = input().strip()

    # Determine the length of the input line
    n = len(line)

    # Initialize a variable to hold the length of the longest repeated substring found
    repeated_length = 0

    # Loop through different lengths of substrings from 0 to n-1
    for length in range(n):
        # Check for substrings of the current length
        for start_index in range(n - length):  # adjust range to avoid out-of-bounds
            # Extract a substring from the current start index
            substring = line[start_index:start_index + length]

            # Check if the substring occurs again later in the string
            if substring in line[start_index + 1:]:  # search ahead in the string
                # Update the result with the current length
                repeated_length = length
                break  # Exit inner loop if a repeat is found

    # Output the length of the longest repeated substring
    print(repeated_length)

# Call the function to execute the code
longest_repeated_substring()
