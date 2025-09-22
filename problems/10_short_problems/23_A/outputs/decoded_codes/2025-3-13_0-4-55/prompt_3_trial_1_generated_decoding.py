def longest_repeated_substring():
    # Read input line from standard input
    n = input()

    # Determine the length of the input line
    l = len(n)
    
    # Initialize variable to hold the result
    m = 0

    # Loop through possible substring lengths from 0 to l - 1
    for s in range(l):
        # Check for repeated substrings of the current length
        for start in range(l):
            # Only proceed if the substring length does not exceed available characters
            if start + s <= l:
                # Extract the substring starting at start with length s
                c = n[start:start + s]

                # Search for the current substring in the remainder of the input line
                if c in n[start + 1:]:
                    # Update the longest repeated substring length
                    m = s
                    break  # Exit the inner loop if a repeat is found

    # Output the length of the longest repeated substring found
    print(m)

# To invoke the function
longest_repeated_substring()
