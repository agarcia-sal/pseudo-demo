def find_longest_repeated_substring():
    # Read a line of input from the user
    line = input().strip()  # Remove any leading/trailing whitespace including newlines
    
    n = len(line)  # Determine the length of the input line
    rv = 0  # Initialize the result variable

    # Loop through all possible lengths of substrings from 0 to n-1
    for l in range(n):  # Iterating length of the substring
        for i in range(n):  # Iterating starting index of the substring
            # Extract the substring
            substring = line[i:i + l]  # Get substring of length l starting at index i
            
            # Check if the substring occurs again in the line
            if substring in line[i + 1:]:  # Check after index i
                rv = l  # Update result variable with the current length l
                break  # Exit the inner loop

    # Output the result variable indicating the length of the longest repeated substring found
    print(rv)

# Call the function to execute
find_longest_repeated_substring()
