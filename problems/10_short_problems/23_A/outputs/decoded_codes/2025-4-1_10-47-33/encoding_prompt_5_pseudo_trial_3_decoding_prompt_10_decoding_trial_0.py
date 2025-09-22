def longest_repeated_substring_length():
    # Read a line of input from the user
    line = input().strip()  # Remove any surrounding whitespace including newlines
    
    # Calculate the length of the input string
    n = len(line)
    
    # Initialize a variable to hold the length of the longest repeated substring
    longest_repeated_length = 0
    
    # Loop through substrings of increasing lengths
    for length in range(1, n):  # Start from length 1 to n-1
        found = False  # Flag to check if any repeat found for this length
        
        # Check all starting positions for the substring of the current length
        for start_position in range(n - length + 1):  # Ensure substring doesn't overflow
            # Extract the substring from 'start_position' of 'length'
            current_substring = line[start_position:start_position + length]
            
            # Check if this substring appears again in the string after its starting position
            if line.find(current_substring, start_position + 1) != -1:
                # If the substring is found again, update the longest repeated length
                longest_repeated_length = length
                found = True  # Indicate that we've found a repeat
                break  # Exit this inner loop as we found a repeat
        
        if found:
            continue  # Skip to the next length if a repeat was found
    
    # Print the length of the longest repeated substring found
    print(longest_repeated_length)

# Call the function to execute the code
longest_repeated_substring_length()
