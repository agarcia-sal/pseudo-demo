def longest_repeated_substring():
    # Read input line from standard input
    n = input()
    
    # Determine the length of the input line
    l = len(n)
    
    # Initialize variable to hold the length of the longest repeated substring
    max_length = 0

    # Loop through possible substring lengths from 1 to l // 2
    for s in range(1, l):
        found = False

        # Check for repeated substrings of the current length
        for start in range(l - s):
            # Extract the substring starting at start with length s
            current_substring = n[start:start + s]

            # Search for the current_substring in the remainder of the input line
            if current_substring in n[start + 1:]:
                # Update the longest repeated substring length
                max_length = s
                found = True
                break  # Exit the inner loop if a repeat is found

        # Break the outer loop if a repeat was found for the current length  
        if found:
            continue

    # Output the length of the longest repeated substring found
    print(max_length)

# Example usage (uncomment below line to test):
# longest_repeated_substring()
