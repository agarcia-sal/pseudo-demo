# Function to find the length of the longest repeated substring
def longest_repeated_substring():
    # Read a line of input and remove the trailing newline character
    line = input().strip()
    n = len(line)  # Get the length of the input string
    longest_repeated_length = 0  # Initialize the variable to store longest repeated length

    # Iterate through possible lengths of substrings
    for length in range(1, n):  # Start from 1 to avoid empty substring
        # Check for repeated substrings of the current length
        for start_index in range(n - length):  # Ensure substring stays within bounds
            # Extract the substring
            substring = line[start_index:start_index + length]

            # Check if the substring occurs again after the current index
            if substring in line[start_index + 1:]:
                longest_repeated_length = length  # Update longest length
                break  # Break the inner loop once a repeated substring is found

    # Output the length of the longest repeated substring
    print(longest_repeated_length)

# Calling the function to execute
longest_repeated_substring()
