def find_longest_repeated_substring():
    line = input()  # Read input from the user
    n = len(line)  # Get the length of the input string
    longest_repetition_length = 0  # Initialize the length of the longest repetition

    # Loop through possible substring lengths from 1 to n-1
    for length in range(1, n):
        # Loop through the starting position of the substring
        for start_position in range(n - length):  # Ensure the substring fits within the string
            substring = line[start_position:start_position + length]  # Extract the substring
            
            # Check if this substring occurs again in the line after the current position
            if substring in line[start_position + length:]:
                longest_repetition_length = length  # Update the longest repetition length
                break  # Break out of the inner loop if a repetition is found

    # Output the length of the longest repeated substring found
    print(longest_repetition_length)

# Example of calling the function (you may uncomment to test)
# find_longest_repeated_substring()
