def find_longest_repeated_substring():
    # Read a line of input (excluding the newline character)
    line = input().strip()
    
    # Determine the length of the input line
    line_length = len(line)
    
    # Initialize a variable to store the result
    longest_repeated_substring_length = 0

    # Loop through all possible lengths of substrings from 1 to line_length
    for length_index in range(1, line_length):
        # Loop through each starting position of the substring
        for start_index in range(line_length - length_index):
            # Extract the substring from the current start index of the current length
            current_substring = line[start_index:start_index + length_index]
            
            # Check if the substring appears again in the line starting after its current position
            if line.find(current_substring, start_index + 1) != -1:
                # If found, update the result with the current length
                longest_repeated_substring_length = length_index
                
                # Exit the inner loop since we found a repeated substring
                break

    # Output the length of the longest repeated substring
    print(longest_repeated_substring_length)

# Example of how to call the function
# Uncomment the line below if you want to run the function:
# find_longest_repeated_substring()
