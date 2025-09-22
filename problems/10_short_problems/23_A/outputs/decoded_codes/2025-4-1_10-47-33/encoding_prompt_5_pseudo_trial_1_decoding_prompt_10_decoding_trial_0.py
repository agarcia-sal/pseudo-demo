def find_longest_repeating_substring():
    # Accept input from the user and remove any trailing whitespace
    input_string = input().strip()
    
    # Determine the length of the input string
    n = len(input_string)
    
    # Initialize variable to track the maximum length of the repeating substring
    maximum_length = 0
    
    # Loop through possible substring lengths from 1 up to n
    for length in range(1, n):  # start from 1 to avoid empty substring
        # Loop through starting positions for the substring
        for start in range(n - length + 1):
            # Extract the substring
            substring = input_string[start:start + length]
            # Check if this substring can be found later in the string
            if substring in input_string[start + length:]:
                maximum_length = length  # Update maximum length
                break  # No need to check further for this length

    # Output the result - the maximum length of a repeating substring found
    print(maximum_length)

# Call the function to execute the program
find_longest_repeating_substring()
