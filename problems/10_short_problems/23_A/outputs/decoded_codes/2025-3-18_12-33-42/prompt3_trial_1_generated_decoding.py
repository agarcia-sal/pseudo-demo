def find_longest_repeated_substring():
    # Read a line of input from standard input
    line = input().rstrip()  # Remove the last character (assuming intended)
    n = len(line)  # Get the length of the line
    return_value = 0  # Initialize the variable for the longest repeated substring length

    # Loop over substring lengths from 0 to n-1
    for l in range(n):
        # Loop over each starting index for the substrings
        for i in range(n):
            if line[i:i+l] in line[i+1:]:  # Check for the substring in the remaining part of the string
                return_value = l  # Update return_value with the found length
                break  # Exit the inner loop when a repeated substring is found
        
        if return_value != 0:  # If a match was found with length l, exit the outer loop
            break

    # Output the longest found length of repeated substring
    print(return_value)

# Call the function to execute
find_longest_repeated_substring()
