def find_longest_repeated_substring():
    # Read a line of input from the user and strip the newline character
    line = input().strip()
    
    # Determine the length of the input line
    n = len(line)
    rv = 0  # Initialize the result variable to hold the length of the longest substring

    # Loop through all possible lengths of substrings from 0 to n-1
    for l in range(n):
        # Loop through the starting index of the substring
        for i in range(n):
            # Ensure the substring of the current length does not exceed the input length
            if i + l < n:
                # Create the substring
                substring = line[i:i + l + 1]
                # Check if the substring appears later in the string
                if line.find(substring, i + 1) != -1:
                    rv = l + 1  # Update result variable with the current length l + 1
                    break  # Exit the inner loop once we find a match
        else:
            continue  # Continue to the next length
        break  # Exit the outer loop if we found a repeated substring

    # Print the result variable indicating the length of the longest repeated substring found
    print(rv)

# Call the function to execute
find_longest_repeated_substring()
