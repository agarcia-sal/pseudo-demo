# Function to find the length of the longest repeated substring
def longest_repeated_substring():
    # Read a line of input from the user
    line = input()
    
    # Removing any trailing newline characters
    line = line.rstrip('\n')
    
    # Calculate the length of the input string
    n = len(line)
    
    # Variable to hold the length of the longest repeated substring found
    longest_repeated_length = 0
    
    # Loop through potential lengths of the substrings
    for length in range(1, n):  # Start from 1 since a length of 0 does not make sense for substrings
        # Check all starting positions for the substring of the current length
        for start_position in range(n - length + 1):  # Substrings can only start from 0 to n-length
            # Extract the current substring from the string
            current_substring = line[start_position:start_position + length]
            
            # Check if this substring appears again in the string after its starting position
            if line.find(current_substring, start_position + 1) != -1:
                # If found again, update the longest repeated length
                longest_repeated_length = length
                break  # Exit this inner loop as we found a repeat

    # Print the length of the longest repeated substring found
    print(longest_repeated_length)

# Calling the function to execute
longest_repeated_substring()
