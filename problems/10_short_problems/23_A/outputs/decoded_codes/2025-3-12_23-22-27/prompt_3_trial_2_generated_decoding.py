def longest_repeated_substring_length():
    # Read input line from standard input
    n = input()
    
    # Determine the length of the input line
    l = len(n)
    
    # Initialize variable to hold the result
    m = 0

    # Loop through possible substring lengths from 1 to l - 1
    for s in range(1, l):  # Starting from 1 as we are looking for repeated substrings
        # Check for repeated substrings of the current length
        for start in range(l - s):  # Ensure we don't go out of bounds
            # Extract the substring starting at 'start' with length 's'
            current_substring = n[start:start + s]
            
            # Search for the current substring in the remainder of the input line
            if current_substring in n[start + 1:]:
                # Update the longest repeated substring length
                m = s
                break  # Exit the inner loop if a repeat is found
    
    # Output the length of the longest repeated substring found
    print(m)

# Call the function to execute
longest_repeated_substring_length()
