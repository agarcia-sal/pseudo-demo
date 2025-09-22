def longest_repeated_substring():
    # Read input line from standard input
    n = input()
    
    # Determine the length of the input line
    l = len(n)
    
    # Initialize variable to hold the result
    longest_length = 0

    # Loop through possible substring lengths from 0 to l - 1
    for s in range(1, l):  # Substring length must be at least 1
        # Check for repeated substrings of the current length
        for start in range(l - s + 1):  # Valid starting positions for substring of length s
            # Extract the substring starting at start with length s
            substring = n[start:start + s]

            # Search for substring in the remainder of the input line
            if substring in n[start + 1:]:  # Look for substring after the current position
                longest_length = s
                break  # Exit the inner loop if a repeat is found
        
        # If a repeated substring is found for current length, no need to check longer lengths
        if longest_length == s:
            continue

    # Output the length of the longest repeated substring found
    print(longest_length)

# Call the function to run
longest_repeated_substring()
