def find_longest_repeated_substring():
    line = input()  # Read a string input
    n = len(line)  # Get the length of the string
    longest_repetition_length = 0  # Initialize the length of the longest repetition to 0

    # Loop through possible substring lengths from 0 to n-1
    for length in range(n):  # Equivalent to FOR length FROM 0 TO n-1
        # Loop through the starting position of the substring
        for start_position in range(n):  # Equivalent to FOR start_position FROM 0 TO n-1
            # Extract the substring of the current length
            substring = line[start_position:start_position + length]  # Get the substring
            
            # Check if this substring occurs again in the line
            if substring in line[start_position + 1:]:  # Check existence in the remaining string
                longest_repetition_length = length  # Update the longest repetition length
                break  # Exit the inner loop
        # No need for additional break as it's already within the inner loop

    # Output the length of the longest repeated substring found
    print(longest_repetition_length)  # Print the result

# To call the function
find_longest_repeated_substring()
