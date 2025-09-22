def find_longest_repeated_substring():
    # Read input string from user
    line = input()
    
    # Get the length of the input string
    n = len(line)
    
    # Initialize the longest repetition length to 0
    longest_repetition_length = 0

    # Loop through possible substring lengths from 0 to n-1
    for length in range(n):
        # Loop through the starting position of the substring
        for start_position in range(n):
            # Extract the substring of the current length
            substring = line[start_position:start_position + length]
            
            # Check if this substring occurs again in the line
            if line.find(substring, start_position + 1) != -1:
                longest_repetition_length = length
                break  # Exit the inner loop if a repetition is found
        else:
            continue  # Continue outer loop if inner loop is not broken
        break  # Exit outer loop if inner loop is broken

    # Output the length of the longest repeated substring found
    print(longest_repetition_length)

# Example test cases (can be uncommented for testing)
# find_longest_repeated_substring()  # Test with an input string
