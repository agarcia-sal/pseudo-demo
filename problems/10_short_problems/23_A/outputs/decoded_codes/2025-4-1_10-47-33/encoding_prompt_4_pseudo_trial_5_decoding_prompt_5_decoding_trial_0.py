# Function to find the length of the longest repeated substring
def length_of_longest_repeated_substring():
    # Read a line of input and remove the trailing newline character
    line = input().strip()
    
    # Determine the length of the input line
    n = len(line)
    
    # Initialize a variable to hold the length of the longest repeated substring
    repeated_length = 0

    # Loop through lengths of substrings from 0 to n-1
    for length in range(n):
        # Check for substrings of the current length
        for start_index in range(n - length):
            # Extract a substring from the current start index
            substring = line[start_index:start_index + length + 1]
            
            # Check if the substring occurs again later in the string
            if substring in line[start_index + 1:]:
                # Update the result with the current length
                repeated_length = length + 1  # length + 1 accounts for the current length
                break  # Exit inner loop if a repeat is found
        
    # Output the length of the longest repeated substring
    print(repeated_length)

# Example test case (commented out)
# Input: abca
# Expected output: 2
# length_of_longest_repeated_substring()  # Uncomment to test with the input
