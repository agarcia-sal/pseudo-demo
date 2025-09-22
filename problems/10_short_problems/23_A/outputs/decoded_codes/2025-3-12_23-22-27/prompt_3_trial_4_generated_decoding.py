def longest_repeated_substring_length():
    # Read input line from standard input
    n = input()
    
    # Determine the length of the input line
    l = len(n)
    
    # Initialize variable to hold the length of the longest repeated substring
    longest_length = 0

    # Loop through possible substring lengths from 1 to l - 1
    for s in range(1, l):
        # Flag to check if we found a repeated substring of the current length
        found_repeated = False
        
        # Check all starting positions for a substring of the current length
        for start in range(l - s + 1):
            # Extract the current substring
            substring = n[start:start + s]
            
            # Check if the current substring appears later in the string
            if substring in n[start + 1:]:
                # Update the longest_length if a repeat is found
                longest_length = s
                found_repeated = True
                break  # Exit the inner loop if a repeat is found
        
        # If a repeated substring is found of the current length, check longer lengths
        if found_repeated:
            continue

    # Output the length of the longest repeated substring found
    print(longest_length)

# Call the function
longest_repeated_substring_length()
