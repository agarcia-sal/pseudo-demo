def find_longest_repeated_substring():
    # Read input line from standard input
    n = input()
    
    # Determine the length of the input line
    l = len(n)
    
    # Initialize variable to hold the result
    longest_length = 0

    # Loop through possible substring lengths from 1 to l - 1
    for substring_length in range(1, l):
        # Check for repeated substrings of the current length
        for start in range(l - substring_length):
            # Extract the substring starting at start with the current length
            current_substring = n[start:start + substring_length]

            # Search for the current substring in the remainder of the input line
            if current_substring in n[start + 1:]:
                # Update the longest repeated substring length
                longest_length = substring_length
                break  # Exit the inner loop if a repeat is found

    # Output the length of the longest repeated substring found
    print(longest_length)

# Example call to the function; uncomment the next line to run the function
# find_longest_repeated_substring()
