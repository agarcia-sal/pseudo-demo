def longest_repeated_substring():
    # Read input line from standard input
    n = input()
    
    # Determine the length of the input line
    l = len(n)
    
    # Initialize variable to hold the length of the longest repeated substring
    longest_repeated_length = 0

    # Loop through possible substring lengths from 1 to l - 1
    for s in range(1, l):
        # Check for repeated substrings of the current length
        for start in range(l - s):
            # Extract the substring starting at start with length s
            substring = n[start:start + s]
            
            # Search for the substring in the remainder of the input line
            if substring in n[start + 1:]:
                # Update the longest repeated substring length
                longest_repeated_length = s
                break  # Exit the inner loop if a repeat is found

    # Output the length of the longest repeated substring found
    print(longest_repeated_length)

# Call the function to execute
longest_repeated_substring()
