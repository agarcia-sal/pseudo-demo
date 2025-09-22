def find_longest_repeated_substring():
    # Read a line of input (excluding newline character)
    line = input().strip()
    length_of_line = len(line)  # Determine the length of the input line
    longest_repeated_length = 0   # Initialize variable to track the longest repeated substring length

    # Iterate over possible lengths for substrings
    for current_length in range(1, length_of_line):  # Start from 1 to avoid empty substrings
        # Set to track seen substrings of the current length
        seen_substrings = set()
        
        # Check for each starting position within the line
        for start_index in range(length_of_line - current_length + 1):  # Ensure valid substring extraction
            # Extract the substring of current_length starting at start_index
            substring = line[start_index:start_index + current_length]

            # Check if the substring has been seen before
            if substring in seen_substrings:
                longest_repeated_length = current_length  # Update longest repeated length if repeat is found
                break  # Exit the inner loop if a repeat is found
            
            # Add substring to the seen set for future comparisons
            seen_substrings.add(substring)

    # Output the length of the longest repeated substring
    print(longest_repeated_length)

# Example testing cases
# To test the function reliably, the input() method can be simulated, 
# or input should be given directly to a console during execution.

